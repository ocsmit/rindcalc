import os
from glob import glob
import numpy as np
from osgeo import gdal
from rindcalc.utils import save_index


def save_comp(bands, out, snap, dType=gdal.GDT_Byte):

    if not os.path.exists(out):
        print('Writing raster')

    if os.path.exists(out):
        os.remove(out)
        print('Overwriting raster.')

    driver = gdal.GetDriverByName('GTiff')
    metadata = driver.GetMetadata()
    shape = bands[0].shape
    dst_ds = driver.Create(out,
                           xsize=shape[1],
                           ysize=shape[0],
                           bands=3,
                           eType=dType)
    proj = snap.GetProjection()
    geo = snap.GetGeoTransform()
    dst_ds.SetGeoTransform(geo)
    dst_ds.SetProjection(proj)
    dst_ds.GetRasterBand(1).WriteArray(bands[0])
    dst_ds.GetRasterBand(2).WriteArray(bands[1])
    dst_ds.GetRasterBand(3).WriteArray(bands[2])
    dst_ds.FlushCache()
    dst_ds = None


class NAIP:

    def __init__(self, path):

        self.bands = {}
        self.path = path

        self.band_options = ['band_1', 'band_2',
                             'band_3' ,'band_4']

    def load_bands(self, which_bands=None):

        bands = {}
        naip = gdal.Open(self.path)
        if which_bands is None:
            which_bands = self.band_options
        for i in range(len(which_bands)):
            if which_bands[i] == 'band_1':
                band_1 = naip.GetRasterBand(1).ReadAsArray().astype(np.float32)
                bands.update({"band_1": band_1})
            if which_bands[i] == 'band_2':
                band_2 = naip.GetRasterBand(2).ReadAsArray().astype(np.float32)
                bands.update({"band_2": band_2})
            if which_bands[i] == 'band_3':
                band_3 = naip.GetRasterBand(3).ReadAsArray().astype(np.float32)
                bands.update({"band_3": band_3})
            if which_bands[i] == 'band_4':
                band_4 = naip.GetRasterBand(4).ReadAsArray().astype(np.float32)
                bands.update({"band_4": band_4})

        snap = naip
        bands.update({"snap": snap})

        self.bands = bands
        return self.bands

    def composite(self, which_bands, out_composite):

        bands = []
        naip = gdal.Open(self.path)
        for i in range(len(which_bands)):
            if which_bands[i] == 'band_1':
                band_1 = naip.GetRasterBand(1).ReadAsArray().astype(np.float32)
                bands.append(band_1)
            if which_bands[i] == 'band_2':
                band_2 = naip.GetRasterBand(2).ReadAsArray().astype(np.float32)
                bands.append(band_2)
            if which_bands[i] == 'band_3':
                band_3 = naip.GetRasterBand(3).ReadAsArray().astype(np.float32)
                bands.append(band_3)
            if which_bands[i] == 'band_4':
                band_4 = naip.GetRasterBand(4).ReadAsArray().astype(np.float32)
                bands.append(band_4)

        save_comp(bands, out_composite, naip)

    def NDVI(self, out_raster=None):
        """
        NDVI(in_naip, ndvi_out, mask_clouds=False)

        Calculates the Normalized Difference Vegetation Index with NAIP imagery
        and outputs a TIFF raster file.

        NDVI = ((NIR - Red) / (NIR + Red))

        Parameters:

                in_naip :: str, required
                    * File path for NAIP image.

                ndvi_out :: str, optional (default=None)
                    * Output path and file name for calculated index raster.
        """

        gdal.PushErrorHandler('CPLQuietErrorHandler')
        gdal.UseExceptions()
        gdal.AllRegister()
        np.seterr(divide='ignore', invalid='ignore')

        bands = self.load_bands(['band_1', 'band_4'])

        # Perform Calculation
        equation = ((bands['band_4'] - bands['band_1']) /
                    (bands['band_4'] + bands['band_1']))

        if out_raster is not None:
            save_index(equation, out_raster, bands['snap'])
            return equation
        if out_raster is None:
            return equation

    def ARVI(self, out_raster=None):
        """
        ARVI(in_naip, arvi_out)

        Calculates the Atmospherically Resistant Vegetation Index with NAIP imagery
        and outputs a TIFF raster file.

        ARVI = (NIR - (2 * Red) + Blue) / (NIR + (2 * Red) + Blue)

        Parameters:

                in_naip :: str, required
                    * File path for NAIP image.

                arvi_out :: str, optional (default=None)
                    * Output path and file name for calculated index raster.
        """

        gdal.PushErrorHandler('CPLQuietErrorHandler')
        gdal.UseExceptions()
        gdal.AllRegister()
        np.seterr(divide='ignore', invalid='ignore')

        bands = self.load_bands(['band_1', 'band_3', 'band_4'])

        # Perform Calculation
        equation = ((bands['band_4'] - (2 * bands['band_1']) + bands['band_3']) /
                    (bands['band_4'] + (2 * bands['band_1']) + bands['band_3']))

        if out_raster is not None:
            save_index(equation, out_raster, bands['snap'])
            return equation
        if out_raster is None:
            return equation

    def VARI(self, out_raster=None):
        """
         VARI(in_naip, vari_out)

        Calculates the Visual Atmospherically Resistant Index with NAIP imagery
        and outputs a TIFF raster file.

        VARI = ((Green - Red) / (Green + Red - Blue))

        Parameters:

                in_naip :: str, required
                    * File path for NAIP image.

                vari_out :: str, optional (default=None)
                    * Output path and file name for calculated index raster.
        """

        gdal.PushErrorHandler('CPLQuietErrorHandler')
        gdal.UseExceptions()
        gdal.AllRegister()
        np.seterr(divide='ignore', invalid='ignore')

        bands = self.load_bands(['band_1', 'band_2', 'band_3'])

        # Perform Calculation
        equation = ((2 * bands['band_2'] - (bands['band_1'] + bands['band_3'])) /
                    (2 * bands['band_2'] + (bands['band_1'] + bands['band_3'])))

        if out_raster is not None:
            save_index(equation, out_raster, bands['snap'])
            return equation
        if out_raster is None:
            return equation

    def SAVI(self, soil_brightness=0.5, out_raster=None):
        """
        SAVI(in_naip, soil_brightness=0.5, savi_out)

        Calculates the Soil Adjusted Vegetation Index with NAIP imagery
        and outputs a TIFF raster file.

        SAVI = ((NIR - Red) / (NIR + Red + L)) x (1 + L)
                                            *L = Soil BrightnessFactor*

        Parameters:

                in_naip :: str, required
                    *File path for NAIP image.

                savi_out :: str, optional (default=None)
                    * Output path and file name for calculated index raster.

                soil_brightness :: float, required (default=0.5)
        """

        gdal.PushErrorHandler('CPLQuietErrorHandler')
        gdal.UseExceptions()
        gdal.AllRegister()
        np.seterr(divide='ignore', invalid='ignore')

        bands = self.load_bands(['band_1', 'band_4'])

        # Perform Calculation
        equation = (((bands['band_4'] - bands['band_1']) / (bands['band_4'] + bands['band_1'] + soil_brightness))
                    * (1 + soil_brightness))

        if out_raster is not None:
            save_index(equation, out_raster, bands['snap'])
            return equation
        if out_raster is None:
            return equation

    def RedRatio(self, out_raster=None):
        """
        Redequation(in_naip, soil_brightness=0.5, savi_out)

        Calculates the Soil Adjusted Vegetation Index with NAIP imagery
        and outputs a TIFF raster file.

        equation = (bands['band_3'] + bands['band_1'] + bands['band_2']) / bands['band_1']

        Parameters:

                in_naip :: str, required
                    * File path for NAIP image.

                redratio_out :: str, optional (default=None)
                    * Output path and file name for calculated index raster.
        """

        gdal.PushErrorHandler('CPLQuietErrorHandler')
        gdal.UseExceptions()
        gdal.AllRegister()
        np.seterr(divide='ignore', invalid='ignore')

        bands = self.load_bands(['band_1', 'band_2', 'band_3'])
        # Perform Calculation
        equation = (bands['band_3'] + bands['band_1'] + bands['band_2']) / bands['band_1']

        if out_raster is not None:
            save_index(equation, out_raster, bands['snap'])
            return equation
        if out_raster is None:
            return equation

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
        """
        Class to read and write NAIP data from.

        Parameters
        ----------
            path : str
                Path to folder where Sentinel-2 bands are contained.

        Attributes
        ----------
            path : dict
                Dictionary of the path for each Landsat-8 band.
            bands : dict, array
                Dictionary of arrays for the bands chosen to load.
            band_options : list
                List of all options for band input names.
        """
        self.bands = {}
        self.path = path

        self.band_options = ['band_1', 'band_2',
                             'band_3','band_4']

    def load_bands(self, which_bands=None):
        """
        Opens and reads bands into Float 32 arrays. If no list is passed into
        `which` bands then all bands are opened and added to the dictionary
        `self.bands`.

        Parameters
        ----------
            which_bands : list, optional
                A list of band names to open as arrays.
                e.g. which_bands=['band_1', 'band_2', 'band_3']

        Returns
        -------
            self.bands : dict
                Updated self.bands dictionary

        """
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

        snap = self.path
        bands.update({"snap": snap})

        self.bands = bands
        return self.bands

    def composite(self, which_bands, out_composite):
        """
        Creates a three band composite out of the specified bands.

        Parameters
        ----------
             which_bands : list
                 A list of bands to save as a three band composite. Must be in
                 order of how the bands are to saved within the output TIFF.
                 e.g. which_bands=['band_1', 'band_2', 'band_3']
             out_composite : str
                 The output filename to save the composite,
        """
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
        Calculates NDVI index

        Parameters
        ----------
            out_raster : str, optional
                Output filepath for calculated TIFF.

        Returns
        -------
            equation : array
                Output array of the generated index.

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
        Calculates ARVI index

        Parameters
        ----------
            out_raster : str, optional
                Output filepath for calculated TIFF.

        Returns
        -------
            equation : array
                Output array of the generated index.

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
        Calculates VARI index

        Parameters
        ----------
            out_raster : str, optional
                Output filepath for calculated TIFF.

        Returns
        -------
            equation : array
                Output array of the generated index.

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
        Calculates SAVI index

        Parameters
        ----------
            soil_brightness : float
                Soil brightness factor to compute SAVI with. Defaults to 0.5
            out_raster : str, optional
                Output filepath for calculated TIFF.

        Returns
        -------
            equation : array
                Output array of the generated index.

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
        Calculates ARVI index

        Parameters
        ----------
            out_raster : str, optional
                Output filepath for calculated TIFF.

        Returns
        -------
            equation : array
                Output array of the generated index.

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

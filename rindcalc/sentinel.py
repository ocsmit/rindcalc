import numpy as np
from osgeo import gdal
import os
from glob import glob
from rindcalc.utils import save_index, resample


class Sentinel:

    def __init__(self, path):
        """
        Class to read and write Sentinel-2 data from.

        Parameters
        ----------
            path : str
                Path to folder where Sentinel-2 bands are contained.

        Attributes
        ----------
            path : dict
                Dictionary of the path for each Sentinel-2 band.
            bands : dict, array
                Dictionary of arrays for the bands chosen to load.
            band_options : list
                List of all options for band input names.
        """
        ends = ['*B01.jp2', '*B02.jp2', '*B03.jp2', '*B04.jp2', '*B05.jp2',
                '*B06.jp2', '*B07.jp2', '*B08.jp2', '*B8A.jp2', '*B09.jp2',
                '*B10.jp2', '*B11.jp2', '*B12.jp2']

        paths = []
        for i in range(len(ends)):
            paths.append(glob(os.path.join(path, ends[i])))
        self.bands = {}
        self.path = {"band_1": paths[0][0], "band_2": paths[1][0],
                     "band_3": paths[2][0], "band_4": paths[3][0],
                     "band_5": paths[4][0], "band_6": paths[5][0],
                     "band_7": paths[6][0], "band_8": paths[7][0],
                     "band_8a": paths[8][0], "band_9": paths[9][0],
                     "band_10": paths[10][0], "band_11": paths[11][0],
                     "band_12": paths[12][0]}
        self.band_options = ['band_1', 'band_2', 'band_3', 'band_4',
                             'band_5', 'band_6', 'band_7', 'band_8',
                             'band_8a', 'band_9', 'band_10', 'band_11',
                             'band_12']

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

        paths = self.path
        bands = {}
        if which_bands is None:
            which_bands = self.band_options
        for i in range(len(which_bands)):
            if which_bands[i] == 'band_1':
                band = gdal.Open(paths["band_1"])
                band_1 = band.GetRasterBand(1).ReadAsArray().astype(
                    np.float32)
                bands.update({"band_1": band_1})
            if which_bands[i] == 'band_2':
                band = gdal.Open(paths["band_2"])
                band_2 = band.GetRasterBand(1).ReadAsArray().astype(
                    np.float32)
                bands.update({"band_2": band_2})
            if which_bands[i] == 'band_3':
                band = gdal.Open(paths["band_3"])
                band_3 = band.GetRasterBand(1).ReadAsArray().astype(
                    np.float32)
                bands.update({"band_3": band_3})
            if which_bands[i] == 'band_4':
                band = gdal.Open(paths["band_4"])
                band_4 = band.GetRasterBand(1).ReadAsArray().astype(
                    np.float32)
                bands.update({"band_4": band_4})
            if which_bands[i] == 'band_5':
                band = gdal.Open(paths["band_5"])
                band_5 = band.GetRasterBand(1).ReadAsArray().astype(
                    np.float32)
                bands.update({"band_5": band_5})
            if which_bands[i] == 'band_6':
                band = gdal.Open(paths["band_6"])
                band_6 = band.GetRasterBand(1).ReadAsArray().astype(
                    np.float32)
                bands.update({"band_6": band_6})
            if which_bands[i] == 'band_7':
                band = gdal.Open(paths["band_7"])
                band_7 = band.GetRasterBand(1).ReadAsArray().astype(
                    np.float32)
                bands.update({"band_7": band_7})
            if which_bands[i] == 'band_8':
                band = gdal.Open(paths["band_8"])
                band_8 = band.GetRasterBand(1).ReadAsArray().astype(
                    np.float32)
                bands.update({"band_8": band_8})
            if which_bands[i] == 'band_8a':
                band = gdal.Open(paths["band_8a"])
                band_8a = band.GetRasterBand(1).ReadAsArray().astype(
                    np.float32)
                bands.update({"band_8a": band_8a})
            if which_bands[i] == 'band_9':
                band = gdal.Open(paths["band_9"])
                band_9 = band.GetRasterBand(1).ReadAsArray().astype(
                    np.float32)
                bands.update({"band_9": band_9})
            if which_bands[i] == 'band_10':
                band = gdal.Open(paths["band_10"])
                band_10 = band.GetRasterBand(1).ReadAsArray().astype(
                    np.float32)
                bands.update({"band_10": band_10})
            if which_bands[i] == 'band_11':
                band = gdal.Open(paths["band_11"])
                band_11 = band.GetRasterBand(1).ReadAsArray().astype(
                    np.float32)
                bands.update({"band_11": band_11})
            if which_bands[i] == 'band_12':
                band = gdal.Open(paths["band_12"])
                band_12 = band.GetRasterBand(1).ReadAsArray().astype(
                    np.float32)
                bands.update({"band_12": band_12})

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

        paths = self.path
        bands = []
        for i in range(len(which_bands)):
            if which_bands[i] == 'band_1':
                bands.append(paths["band_1"])
            if which_bands[i] == 'band_2':
                bands.append(paths["band_2"])
            if which_bands[i] == 'band_3':
                bands.append(paths["band_3"])
            if which_bands[i] == 'band_4':
                bands.append(paths["band_4"])
            if which_bands[i] == 'band_5':
                bands.append(paths["band_5"])
            if which_bands[i] == 'band_6':
                bands.append(paths["band_6"])
            if which_bands[i] == 'band_7':
                bands.append(paths["band_7"])
            if which_bands[i] == 'band_8':
                bands.append(paths["band_8"])
            if which_bands[i] == 'band_8a':
                bands.append(paths["band_8"])
            if which_bands[i] == 'band_9':
                bands.append(paths["band_9"])
            if which_bands[i] == 'band_10':
                bands.append(paths["band_10"])
            if which_bands[i] == 'band_11':
                bands.append(paths["band_11"])
            if which_bands[i] == 'band_12':
                bands.append(paths["band_12"])

        vrt = gdal.BuildVRT('tmp.vrt', bands, separate=True, bandList=[1, 1, 1])
        trans = gdal.Translate(out_composite, vrt, format='GTiff')

    def AWEIsh(self, out_raster=None):
        """
        Calculates AWEIsh index

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

        bands = self.load_bands(["band_2", "band_3", "band_8"])

        band_11 = resample(self.path['band_11'], 10)
        band_12 = resample(self.path['band_12'], 10)

        a = (bands["band_2"] + 2.5 * bands["band_3"] - 1.5 *
             (bands["band_8"] + band_11) - 0.25 *
             band_12)
        b = (bands["band_2"] + bands["band_3"] + bands["band_8"]
             + band_11 + band_12)
        equation = a / b

        snap = self.path['band_2']

        if out_raster is not None:
            save_index(equation, out_raster, snap, gdal.GDT_Float32)
        return equation

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

        bands = self.load_bands(["band_4", "band_8"])

        equation = (bands["band_8"] - bands["band_4"]) / \
                   (bands["band_8"] + bands["band_4"])

        snap = self.path['band_2']

        if out_raster is not None:
            save_index(equation, out_raster, snap, gdal.GDT_Float32)
        return equation

    def SIPI(self, out_raster=None):
        """
        Calculates SIPI index

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

        bands = self.load_bands(["band_2", "band_8"])

        equation = (bands["band_8"] - bands["band_2"]) / \
                   (bands["band_8"] + bands["band_2"])

        snap = self.path['band_2']

        if out_raster is not None:
            save_index(equation, out_raster, snap, gdal.GDT_Float32)
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

        bands = self.load_bands(["band_2", "band_4", "band_8"])

        equation = ((bands["band_8"] - (2 * bands["band_4"]) + bands["band_2"])/
                    (bands["band_8"] + (2 * bands["band_4"]) + bands["band_2"]))

        snap = self.path['band_2']

        if out_raster is not None:
            save_index(equation, out_raster, snap, gdal.GDT_Float32)
        return equation

    def NDI45(self, out_raster=None):
        """
        Calculates NDI45 index

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

        bands = self.load_bands(['band_4'])
        band_5 = resample(self.path['band_5'], 10)

        equation = ((band_5 - bands['band_4']) /
                    (band_5 + bands['band_4']))

        snap = self.path['band_4']

        if out_raster is not None:
            save_index(equation, out_raster, snap, gdal.GDT_Float32)
        return equation

    def MTCI(self, out_raster=None):
        """
        Calculates MTCI index

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

        bands = self.load_bands(['band_4'])
        band_5 = resample(self.path['band_5'], 10)
        band_6 = resample(self.path['band_6'], 10)

        equation = ((band_6 - band_5) /
                    (band_5 - bands['band_4']))

        snap = self.path['band_4']

        if out_raster is not None:
            save_index(equation, out_raster, snap, gdal.GDT_Float32)
        return equation

    def MCARI(self, out_raster=None):
        """
        Calculates MCARI index

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

        bands = self.load_bands(['band_3', 'band_4'])
        band_5 = resample(self.path['band_5'], 10)

        equation = (abs((band_5 - bands['band_4']) - 0.2 *
                    (band_5 - bands['band_3'])) *
                    (band_5 - bands['band_4']))

        snap = self.path['band_4']

        if out_raster is not None:
            save_index(equation, out_raster, snap, gdal.GDT_Float32)
        return equation

    def GNDVI(self, out_raster=None):
        """
        Calculates GNDVI index

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

        bands = self.load_bands(['band_3'])
        band_7 = resample(self.path['band_7'], 10)

        equation = ((band_7 - bands['band_3']) /
                    (band_7 + bands['band_3']))

        snap = self.path['band_3']

        if out_raster is not None:
            save_index(equation, out_raster, snap, gdal.GDT_Float32)
        return equation

    def PSSR(self, out_raster=None):
        """
        Calculates PSSR index

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

        band_7 = resample(self.path['band_7'], 10)
        bands = self.load_bands(['band_4'])

        equation = (band_7 / bands['band_4'])

        snap = self.path['band_4']

        if out_raster is not None:
            save_index(equation, out_raster, snap, gdal.GDT_Float32)
        return equation

    def S2REP(self, out_raster=None):
        """
        Calculates S2REP index

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

        bands = self.load_bands(['band_4'])
        band_5 = resample(self.path['band_5'], 10)
        band_6 = resample(self.path['band_6'], 10)
        band_7 = resample(self.path['band_7'], 10)

        equation = 705 + 35 * ((((band_7 + bands['band_4']) / 2) - band_5) /
                               (band_6 - band_5))

        snap = self.path['band_4']

        if out_raster is not None:
            save_index(equation, out_raster, snap, gdal.GDT_Float32)
        return equation

    def IRECI(self, out_raster=None):
        """
        Calculates IRECI index

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

        bands = self.load_bands(['band_4'])
        band_5 = resample(self.path['band_5'], 10)
        band_6 = resample(self.path['band_6'], 10)
        band_7 = resample(self.path['band_7'], 10)

        equation = ((band_7 - bands['band_4']) / (band_5 / band_6))

        snap = self.path['band_4']

        if out_raster is not None:
            save_index(equation, out_raster, snap, gdal.GDT_Float32)
        return equation

    def SAVI(self, soil_moisture=0.5, out_raster=None):
        """
        Calculates SAVI index

        Parameters
        ----------
            soil_moisture : flt
                Soil moisture value, default = 0.5
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

        bands = self.load_bands(['band_4', 'band_8'])

        equation = (((bands['band_8'] - bands['band_4']) / (bands['band_8'] +
                      bands['band_4'] + soil_moisture)) * (1 + soil_moisture))

        snap = self.path['band_4']

        if out_raster is not None:
            save_index(equation, out_raster, snap, gdal.GDT_Float32)
        return equation




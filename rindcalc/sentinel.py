import numpy as np
from osgeo import gdal
import os
from glob import glob
from rindcalc.utils import save_index, resample


class Sentinel:

    def __init__(self, path):
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

    def AWEIsh(self, out_raster):

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

        snap = gdal.Open(self.path['band_2'])

        if out_raster is not None:
            save_index(equation, out_raster, snap, gdal.GDT_Float32)
        return equation

    def NDVI(self, out_raster):

        gdal.PushErrorHandler('CPLQuietErrorHandler')
        gdal.UseExceptions()
        gdal.AllRegister()
        np.seterr(divide='ignore', invalid='ignore')

        bands = self.load_bands(["band_4", "band_8"])

        equation = (bands["band_8"] - bands["band_4"]) / \
                   (bands["band_8"] + bands["band_4"])

        snap = gdal.Open(self.path['band_2'])

        save_index(equation, out_raster, snap, gdal.GDT_Float32)
        return equation

    def SIPI(self, out_raster):

        gdal.PushErrorHandler('CPLQuietErrorHandler')
        gdal.UseExceptions()
        gdal.AllRegister()
        np.seterr(divide='ignore', invalid='ignore')

        bands = self.load_bands(["band_2", "band_8"])

        equation = (bands["band_8"] - bands["band_2"]) / \
                   (bands["band_8"] + bands["band_2"])

        snap = gdal.Open(self.path['band_2'])

        if out_raster is not None:
            save_index(equation, out_raster, snap, gdal.GDT_Float32)
        return equation

    def ARVI(self, out_raster):

        gdal.PushErrorHandler('CPLQuietErrorHandler')
        gdal.UseExceptions()
        gdal.AllRegister()
        np.seterr(divide='ignore', invalid='ignore')

        bands = self.load_bands(["band_2", "band_4", "band_8"])

        equation = ((bands["band_8"] - (2 * bands["band_4"]) + bands["band_2"])/
                    (bands["band_8"] + (2 * bands["band_4"]) + bands["band_2"]))

        snap = gdal.Open(self.path['band_2'])

        if out_raster is not None:
            save_index(equation, out_raster, snap, gdal.GDT_Float32)
        return equation


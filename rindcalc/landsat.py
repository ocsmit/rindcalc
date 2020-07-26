
import os
from glob import glob
import numpy as np
from osgeo import gdal
from rindcalc.utils import save_index


def cloud_mask(qa_band, array):
    """
    This function masks clouds in Landsat-8 imagery using the QA band and
    returns an array to save as a raster.
    """

    gdal.UseExceptions()
    gdal.AllRegister()
    np.seterr(divide='ignore', invalid='ignore')
    qa_path = gdal.Open(qa_band)
    qa_band = qa_path.GetRasterBand(1).ReadAsArray().astype(np.uint32)

    mask_values = [2800, 2804, 2808, 2812, 6986, 6900, 6904, 6908,
                   2976, 2980, 2984, 2988, 3008, 3012, 3016, 3020,
                   7072, 7076, 7080, 7084, 7104, 7108, 7112, 7116]
    np.seterr(divide='ignore', invalid='ignore')
    m = np.ma.array(qa_band,
                    mask=np.logical_or.reduce([qa_band == value
                                               for value in mask_values]))
    np.ma.set_fill_value(m, 0)
    m1 = m.filled()
    m1[m1 != 0] = 1

    m1.reshape(qa_band.shape)
    mask_array = array * m1
    mask_array[mask_array == 0] = np.nan

    return mask_array


def save_ls(qa_band, equation, out_raster, snap, mask_clouds):
    if out_raster is not None and mask_clouds:
        masked = cloud_mask(qa_band, equation)
        save_index(masked, out_raster, snap)
        return masked
    if out_raster is not None and not mask_clouds:
        save_index(equation, out_raster, snap)
        return equation
    if out_raster is None and mask_clouds:
        masked = cloud_mask(qa_band, equation)
        return masked
    if out_raster is None and not mask_clouds:
        return equation


class Landsat:

    def __init__(self, path):
        ends = ['*B1.TIF', '*B2.TIF', '*B3.TIF', '*B4.TIF', '*B5.TIF',
                '*B6.TIF', '*B7.TIF', '*B8.TIF', '*B9.TIF', '*B10.TIF',
                '*BQA.TIF']

        paths = []
        for i in range(len(ends)):
            paths.append(glob(os.path.join(path, ends[i])))

        self.bands = {}
        self.path = {"band_1": paths[0][0], "band_2": paths[1][0],
                     "band_3": paths[2][0], "band_4": paths[3][0],
                     "band_5": paths[4][0], "band_6": paths[5][0],
                     "band_7": paths[6][0], "band_8": paths[7][0],
                     "band_9": paths[8][0], "band_10": paths[9][0],
                     "band_qa": paths[10][0]}
        self.band_options = ['band_1', 'band_2', 'band_3', 'band_4',
                             'band_5', 'band_6', 'band_7', 'band_8',
                             'band_9', 'band_10', 'band_qa']

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
            if which_bands[i] == 'band_9':
                bands.append(paths["band_9"])
            if which_bands[i] == 'band_10':
                bands.append(paths["band_10"])

        vrt = gdal.BuildVRT('tmp.vrt', bands, separate=True, bandList=[1, 1, 1])
        trans = gdal.Translate(out_composite, vrt, format='GTiff')

    def NDVI(self, out_tif=None, mask_clouds=False):

        gdal.UseExceptions()
        gdal.AllRegister()
        np.seterr(divide='ignore', invalid='ignore')

        bands = self.load_bands(['band_3', 'band_6'])

        equation = ((bands["band_3"] - bands["band_6"]) /
                    (bands["band_3"] + bands["band_6"]))

        snap = gdal.Open(self.path['band_2'])
        out_ras = save_ls(self.path['band_qa'], equation, out_tif,
                          snap, mask_clouds)

        return out_ras

    def AWEIsh(self, out_tif=None, mask_clouds=False):
        """
        AWEIsh(landsat_dir, aweish_out, mask_clouds=False)

        Calculates the Automated Water Extraction Index (shadow) with Landsat-8
        and outputs a TIFF raster file.

        AWEIsh = (Blue + 2.5 * Green - 1.5 * (NIR + SWIR1) - 0.25 *
                    SWIR2) /  (Blue + Green + NIR + SWIR1 + SWIR2)

        Parameters:

                landsat_dir :: str, required
                    * Folder path where all landsat bands for the scene are
                      contained.

                out_tif :: str, optional (default=None)
                    * Output path and file name for calculated index raster.

                mask_clouds :: boolean, optional (default=False)
                    * Whether or not to apply cloud mask to scene based of QA band.

                mask_clouds :: boolean, optional (default=False)
                * Whether or not to apply cloud mask to scene based of QA band.
        """

        gdal.UseExceptions()
        gdal.AllRegister()
        np.seterr(divide='ignore', invalid='ignore')

        bands = self.load_bands(['band_2', 'band_3', 'band_5', 'band_6',
                                'band_7'])

        a = (bands["band_2"] + 2.5 * bands["band_3"] - 1.5 *
             (bands["band_5"] + bands["band_6"]) - 0.25 * bands["band_7"])
        b = (bands["band_2"] + bands["band_2"] + bands["band_5"] + bands[
            "band_6"]
             + bands["band_7"])
        equation = (a / b)

        snap = gdal.Open(self.path['band_2'])
        out_ras = save_ls(self.path['band_qa'], equation, out_tif,
                          snap, mask_clouds)

        return out_ras

    def AWEInsh(self, out_tif=None, mask_clouds=False):
        """
        AWEInsh(landsat_dir, aweinsh_out, mask_clouds=False)

        Calculates the Automated Water Extraction Index (no shadow) with Landsat-8
        and outputs a TIFF raster file.

        AWEInsh = (4 * (Green - SWIR1) - (0.25 * NIR + 2.75 *
                    SWIR1)) /  (Green + SWIR1 + NIR)

        Parameters:

                landsat_dir :: str, required
                    * Folder path where all landsat bands for the scene are
                      contained.

                out_tif :: str, optional (default=None)
                    * Output path and file name for calculated index raster.

                mask_clouds :: boolean, optional (default=False)
                    * Whether or not to apply cloud mask to scene based of QA band.

                mask_clouds :: boolean, optional (default=False)
                    * Whether or not to apply cloud mask to scene based of QA band.
        """

        gdal.UseExceptions()
        gdal.AllRegister()
        np.seterr(divide='ignore', invalid='ignore')

        bands = self.load_bands(['band_3', 'band_5', 'band_6',
                                'band_7'])

        equation = ((4 * (bands["band_3"] - bands["band_6"]) -
                     (0.25 * bands["band_5"] + 2.75 * bands["band_6"])) /
                    (bands["band_3"] + bands["band_6"] + bands["band_5"]))

        snap = gdal.Open(self.path['band_2'])
        out_ras = save_ls(self.path['band_qa'], equation, out_tif,
                          snap, mask_clouds)

        return out_ras

    def NDMI(self, out_tif=None, mask_clouds=False):
        """
        NDMI(landsat_dir, ndmi_out)

        Calculates the Normalized Difference Moisture Index with Landsat-8
        and outputs a TIFF raster file.

        NDMI = (NIR - SWIR1) / (NIR + SWIR1)

        Parameters:

                landsat_dir :: str, required
                    * Folder path where all landsat bands for the scene are
                      contained.

                out_tif :: str, optional (default=None)
                    * Output path and file name for calculated index raster.

                mask_clouds :: boolean, optional (default=False)
                    * Whether or not to apply cloud mask to scene based of QA band.
        """

        gdal.UseExceptions()
        gdal.AllRegister()
        np.seterr(divide='ignore', invalid='ignore')

        bands = self.load_bands(['band_5', 'band_6'])

        equation = ((bands["band_5"] - bands["band_6"]) /
                    (bands["band_5"] + bands["band_6"]))

        snap = gdal.Open(self.path['band_2'])
        out_ras = save_ls(self.path['band_qa'], equation, out_tif,
                          snap, mask_clouds)
        return out_ras

    def MNDWI(self, out_tif=None, mask_clouds=False):
        """
        MNDWI(landsat_dir, mndwi_out)

        Calculates the Modified Normalized Difference Water Index with Landsat-8
        and outputs a TIFF raster file.

        MNDWI = (Green - SWIR1) / (Green + SWIR1)

        Parameters:

                landsat_dir :: str, required
                    * Folder path where all landsat bands for the scene are
                      contained.

                out_tif :: str, optional (default=None)
                    * Output path and file name for calculated index raster.

                mask_clouds :: boolean, optional (default=False)
                    * Whether or not to apply cloud mask to scene based of QA band.
        """

        gdal.UseExceptions()
        gdal.AllRegister()
        np.seterr(divide='ignore', invalid='ignore')

        bands = self.load_bands(['band_3', 'band_6'])

        equation = ((bands["band_3"] - bands["band_6"]) /
                    (bands["band_3"] + bands["band_6"]))

        snap = gdal.Open(self.path['band_2'])
        out_ras = save_ls(self.path['band_qa'], equation, out_tif,
                          snap, mask_clouds)
        return out_ras

    def GNDVI(self, out_tif=None, mask_clouds=False):
        """
        GNDVI(landsat_dir, gndvi_out)

        Calculates the Green Normalized Difference Vegetation Index with Landsat-8
        and outputs a TIFF raster file.

        GNDVI = (NIR - Green) / (NIR + Green)

        Parameters:

                landsat_dir :: str, required
                    * Folder path where all landsat bands for the scene are
                      contained.

                gndvi_out :: str, optional (default=None)
                    * Output path and file name for calculated index raster.

                mask_clouds :: boolean, optional (default=False)
                    * Whether or not to apply cloud mask to scene based of QA band.
        """

        gdal.UseExceptions()
        gdal.AllRegister()
        np.seterr(divide='ignore', invalid='ignore')

        bands = self.load_bands(['band_5', 'band_3'])

        equation = ((bands["band_5"] - bands["band_3"])
                    / (bands["band_5"] + bands["band_3"]))

        snap = gdal.Open(self.path['band_2'])
        out_ras = save_ls(self.path['band_qa'], equation, out_tif,
                          snap, mask_clouds)
        return out_ras

    def SAVI(self, out_tif=None, soil_brightness=0.5, mask_clouds=False):
        """
        SAVI(landsat_dir, soil_brightness=0.5, savi_out)

        Calculates the Soil Adjusted Vegetation Index with Landsat-8
        and outputs a TIFF raster file.

        SAVI = ((NIR - Red) / (NIR + Red + L)) x (1 + L)
                                            *L = Soil BrightnessFactor*

        Parameters:

                landsat_dir :: str, required
                    * Folder path where all landsat bands for the scene are
                      contained.

                out_tif :: str, optional (default=None)
                    * Output path and file name for calculated index raster.

                soil_brightness :: float, required (default=0.5)

                 mask_clouds :: boolean, optional (default=False)
                    * Whether or not to apply cloud mask to scene based of QA band.
        """

        gdal.UseExceptions()
        gdal.AllRegister()
        np.seterr(divide='ignore', invalid='ignore')

        bands = self.load_bands(['band_5', 'band_4'])

        equation = ((bands["band_5"] - bands["band_4"]) /
                    (bands["band_5"] + bands["band_4"] + soil_brightness)) \
                    * (1 + soil_brightness)

        snap = gdal.Open(self.path['band_2'])
        out_ras = save_ls(self.path['band_qa'], equation, out_tif,
                          snap, mask_clouds)

        return out_ras

    def ARVI(self, out_tif=None, mask_clouds=False):
        """
        ARVI(landsat_dir, arvi_out)

        Calculates the Atmospherically Resistant Vegetation Index with Landsat-8
        and outputs a TIFF raster file.

        ARVI = (NIR - (2 * Red) + Blue) / (NIR + (2 * Red) + Blue)

        Parameters:

                landsat_dir :: str, required
                    * Folder path where all landsat bands for the scene are
                      contained.

                out_tif :: str, optional (default=None)
                    * Output path and file name for calculated index raster.

                mask_clouds :: boolean, optional (default=False)
                    * Whether or not to apply cloud mask to scene based of QA band.
        """

        gdal.UseExceptions()
        gdal.AllRegister()
        np.seterr(divide='ignore', invalid='ignore')

        bands = self.load_bands(['band_2', 'band_4', 'band_5'])

        equation = ((bands["band_5"] - (2 * bands["band_4"]) + bands[
            "band_2"]) /
                    (bands["band_5"] + (2 * bands["band_4"]) + bands["band_2"]))

        snap = gdal.Open(self.path['band_2'])
        out_ras = save_ls(self.path['band_qa'], equation, out_tif,
                          snap, mask_clouds)

        return out_ras

    def VARI(self, out_tif=None, mask_clouds=False):
        """
        VARI(landsat_dir, vari_out)

        Calculates the Visual Atmospherically Resistant Index with Landsat-8
        and outputs a TIFF raster file.

        VARI = ((Green - Red) / (Green + Red - Blue))

        Parameters:

                landsat_dir :: str, required
                    * Folder path where all landsat bands for the scene are
                      contained.

                out_tif :: str, optional (default=None)
                    * Output path and file name for calculated index raster.

                mask_clouds :: boolean, optional (default=False)
                    * Whether or not to apply cloud mask to scene based of QA band.
        """

        gdal.UseExceptions()
        gdal.AllRegister()
        np.seterr(divide='ignore', invalid='ignore')

        bands = self.load_bands(['band_2', 'band_3', 'band_4'])

        equation = ((bands["band_3"] - bands["band_4"]) /
                    (bands["band_3"] + bands["band_4"] - bands["band_2"]))

        snap = gdal.Open(self.path['band_2'])
        out_ras = save_ls(self.path['band_qa'], equation, out_tif,
                          snap, mask_clouds)

        return out_ras

    def NDBI(self, out_tif=None, mask_clouds=False):
        """
        NDBI(landsat_dir, ndbi_out)

        Calculates the Normalized Difference Built-up Index with Landsat-8
        and outputs a TIFF raster file.

        NDBI = (SWIR1 - NIR) / (SWIR1 + NIR)

        Parameters:

                landsat_dir :: str, required
                    * Folder path where all landsat bands for the scene are
                      contained.

                out_tif :: str, optional (default=None)
                    * Output path and file name for calculated index raster.

                mask_clouds :: boolean, optional (default=False)
                    * Whether or not to apply cloud mask to scene based of QA band.
        """

        gdal.UseExceptions()
        gdal.AllRegister()
        np.seterr(divide='ignore', invalid='ignore')

        bands = self.load_bands(['band_5', 'band_6'])

        # Perform Calculation
        equation = ((bands["band_6"] - bands["band_5"]) / (
                    bands["band_6"] + bands["band_5"]))

        snap = gdal.Open(self.path['band_2'])
        out_ras = save_ls(self.path['band_qa'], equation, out_tif,
                          snap, mask_clouds)
        return out_ras

    def NDBaI(self, out_tif=None, mask_clouds=False):
        """
        NDBaI(landsat_dir, ndbai_out)

        Calculates the Normalized Difference Bareness Index with Landsat-8
        and outputs a TIFF raster file.

        NDBaI = ((SWIR1 - TIR) / (SWIR1 + TIR))

        Parameters:

                landsat_dir :: str, required
                    * Folder path where all landsat bands for the scene are
                      contained.

                out_tif :: str, optional (default=None)
                    * Output path and file name for calculated index raster.

                mask_clouds :: boolean, optional (default=False)
                    * Whether or not to apply cloud mask to scene based of QA band.
        """

        gdal.UseExceptions()
        gdal.AllRegister()
        np.seterr(divide='ignore', invalid='ignore')

        bands = self.load_bands(['band_6', 'band_10'])

        # Perform Calculation
        equation = ((bands["band_6"] - bands["band_10"]) /
                    (bands["band_6"] + bands["band_10"]))

        snap = gdal.Open(self.path['band_2'])
        out_ras = save_ls(self.path['band_qa'], equation, out_tif,
                          snap, mask_clouds)
        return out_ras

    def NBLI(self, out_tif=None, mask_clouds=False):
        """
        NBLI(landsat_dir, nbli_out)

        Calculates the Normalized Difference Bareland Index with Landsat-8
        and outputs a TIFF raster file.

        NBLI = (Red - TIR) / (Red + TIR)

        Parameters:

                landsat_dir :: str, required
                    * Folder path where all landsat bands for the scene are
                      contained.

                out_tif :: str, optional (default=None)
                    * Output path and file name for calculated index raster.

                mask_clouds :: boolean, optional (default=False)
                    * Whether or not to apply cloud mask to scene based of QA band.
        """

        gdal.UseExceptions()
        gdal.AllRegister()
        np.seterr(divide='ignore', invalid='ignore')

        bands = self.load_bands(['band_4', 'band_10'])

        equation = ((bands["band_4"] - bands["band_10"]) /
                    (bands["band_4"] + bands["band_10"]))

        snap = gdal.Open(self.path['band_2'])
        out_ras = save_ls(self.path['band_qa'], equation, out_tif,
                          snap, mask_clouds)
        return out_ras

    def EBBI(self, out_tif=None, mask_clouds=False):
        """
        EBBI(landsat_dir, ebbi_out)

        Calculates the Enhanced Built-up and Bareness Index with Landsat-8
        and outputs a TIFF raster file.

        EBBI = (SWIR1 - NIR) / (10 * (sqrt(SWIR1 + tir)))

        Parameters:

                landsat_dir :: str, required
                    * Folder path where all landsat bands for the scene are
                      contained.

                out_tif :: str, optional (default=None)
                    * Output path and file name for calculated index raster

                mask_clouds :: boolean, optional (default=False)
                    * Whether or not to apply cloud mask to scene based of QA band.
        """

        gdal.UseExceptions()
        gdal.AllRegister()
        np.seterr(divide='ignore', invalid='ignore')

        bands = self.load_bands(['band_5', 'band_6', 'band_7', 'band_10'])

        ebbi = ((bands["band_6"] - bands["band_5"]) /
                (10 * ((bands["band_6"] + bands["band_10"]) ** 0.5)))
        ebbi[np.isneginf(ebbi)] = 0
        ebbi_mask = np.ma.MaskedArray(ebbi, mask=(ebbi == 0))
        ebbi_mask.reshape(ebbi.shape)

        snap = gdal.Open(self.path['band_2'])
        out_ras = save_ls(self.path['band_qa'], ebbi_mask, out_tif,
                          snap, mask_clouds)
        return out_ras

    def UI(self, out_tif=None, mask_clouds=False):
        """
        UI(landsat_dir, ui_out)

        Calculates the Urban Index with Landsat-8 and outputs a TIFF raster file.

        UI = (SWIR2 - NIR) / (SWIR2 + NIR)

        Parameters:

                landsat_dir :: str, required
                    * Folder path where all landsat bands for the scene are
                      contained.

                out_tif :: str, optional (default=None)
                    * Output path and file name for calculated index raster.

                mask_clouds :: boolean, optional (default=False)
                    * Whether or not to apply cloud mask to scene based of QA band.
        """

        gdal.UseExceptions()
        gdal.AllRegister()
        np.seterr(divide='ignore', invalid='ignore')

        bands = self.load_bands(['band_5', 'band_7'])

        # Perform Calculation
        equation = ((bands["band_7"] - bands["band_5"]) /
                    (bands["band_7"] + bands["band_5"]))

        snap = gdal.Open(self.path['band_2'])
        out_ras = save_ls(self.path['band_qa'], equation, out_tif,
                          snap, mask_clouds)
        return out_ras

    def NBRI(self, out_tif=None, mask_clouds=False):
        """
        NBRI(landsat_dir, nbri_out)

        Calculates the Normalized Burn Ratio Index with Landsat-8 and outputs a
        TIFF raster file.

        UI = (SWIR2 - NIR) / (SWIR2 + NIR)

        Parameters:

                landsat_dir :: str, required
                    * Folder path where all landsat bands for the scene are
                      contained.

                out_tif :: str, optional (default=None)
                    * Output path and file name for calculated index raster.

                mask_clouds :: boolean, optional (default=False)
                    * Whether or not to apply cloud mask to scene based of QA band.
        """

        gdal.UseExceptions()
        gdal.AllRegister()
        np.seterr(divide='ignore', invalid='ignore')

        bands = self.load_bands(['band_5', 'band_7'])

        # calculation
        equation = ((bands["band_5"] - bands["band_7"]) /
                    (bands["band_5"] + bands["band_7"]))

        snap = gdal.Open(self.path['band_2'])
        out_ras = save_ls(self.path['band_qa'], equation, out_tif,
                          snap, mask_clouds)
        return out_ras

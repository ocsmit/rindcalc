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
        """
        Class to read and write Landsat-8 data from.


        Parameters
        ----------
            path : str
                Path to folder where Landsat-8 bands are contained.

        Attributes
        ----------
            path : dict
                Dictionary of the path for each Landsat-8 band.
            bands : dict, array
                Dictionary of arrays for the bands chosen to load.
            band_options : list
                List of all options for band input names.
        """
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
            if which_bands[i] == 'band_qa':
                band = gdal.Open(paths["band_qa"])
                band_qa = band.GetRasterBand(1).ReadAsArray().astype(
                    np.float32)
                bands.update({"band_qa": band_qa})

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
            if which_bands[i] == 'band_9':
                bands.append(paths["band_9"])
            if which_bands[i] == 'band_10':
                bands.append(paths["band_10"])

        vrt = gdal.BuildVRT('tmp.vrt', bands, separate=True, bandList=[1, 1, 1])
        trans = gdal.Translate(out_composite, vrt, format='GTiff')

    def NDVI(self, out_raster=None, mask_clouds=False):
        """
        Calculates NDVI index

        Parameters
        ----------
            out_raster : str, optional
                Output filepath for calculated TIFF.
            mask_clouds : bool, optional
                Whether or not to apply cloud masking to output index with
                the QA band.

        Returns
        -------
            equation : array
                Output array of the generated index.

        """
        gdal.UseExceptions()
        gdal.AllRegister()
        np.seterr(divide='ignore', invalid='ignore')

        bands = self.load_bands(['band_3', 'band_6'])

        equation = ((bands["band_3"] - bands["band_6"]) /
                    (bands["band_3"] + bands["band_6"]))

        snap = self.path['band_2']
        out_ras = save_ls(self.path['band_qa'], equation, out_raster,
                          snap, mask_clouds)

        return out_ras

    def AWEIsh(self, out_raster=None, mask_clouds=False):
        """"
        Calculates AWEIsh index

        Parameters
        ----------
            out_raster : str, optional
                Output filepath for calculated TIFF.
            mask_clouds : bool, optional
                Whether or not to apply cloud masking to output index with
                the QA band.

        Returns
        -------
            equation : array
                Output array of the generated index.

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

        snap = self.path['band_2']
        out_ras = save_ls(self.path['band_qa'], equation, out_raster,
                          snap, mask_clouds)

        return out_ras

    def AWEInsh(self, out_raster=None, mask_clouds=False):
        """
        Calculates AWEInsh index

        Parameters
        ----------
            out_raster : str, optional
                Output filepath for calculated TIFF.
            mask_clouds : bool, optional
                Whether or not to apply cloud masking to output index with
                the QA band.

        Returns
        -------
            equation : array
                Output array of the generated index.

        """
        gdal.UseExceptions()
        gdal.AllRegister()
        np.seterr(divide='ignore', invalid='ignore')

        bands = self.load_bands(['band_3', 'band_5', 'band_6',
                                'band_7'])

        equation = ((4 * (bands["band_3"] - bands["band_6"]) -
                     (0.25 * bands["band_5"] + 2.75 * bands["band_6"])) /
                    (bands["band_3"] + bands["band_6"] + bands["band_5"]))

        snap = self.path['band_2']
        out_ras = save_ls(self.path['band_qa'], equation, out_raster,
                          snap, mask_clouds)

        return out_ras

    def NDMI(self, out_raster=None, mask_clouds=False):
        """
        Calculates NDMI index

        Parameters
        ----------
            out_raster : str, optional
                Output filepath for calculated TIFF.
            mask_clouds : bool, optional
                Whether or not to apply cloud masking to output index with
                the QA band.

        Returns
        -------
            equation : array
                Output array of the generated index.

        """
        gdal.UseExceptions()
        gdal.AllRegister()
        np.seterr(divide='ignore', invalid='ignore')

        bands = self.load_bands(['band_5', 'band_6'])

        equation = ((bands["band_5"] - bands["band_6"]) /
                    (bands["band_5"] + bands["band_6"]))

        snap = self.path['band_2']
        out_ras = save_ls(self.path['band_qa'], equation, out_raster,
                          snap, mask_clouds)
        return out_ras

    def MNDWI(self, out_raster=None, mask_clouds=False):
        """
        Calculates MNDWI index

        Parameters
        ----------
            out_raster : str, optional
                Output filepath for calculated TIFF.
            mask_clouds : bool, optional
                Whether or not to apply cloud masking to output index with
                the QA band.

        Returns
        -------
            equation : array
                Output array of the generated index.

        """
        gdal.UseExceptions()
        gdal.AllRegister()
        np.seterr(divide='ignore', invalid='ignore')

        bands = self.load_bands(['band_3', 'band_6'])

        equation = ((bands["band_3"] - bands["band_6"]) /
                    (bands["band_3"] + bands["band_6"]))

        snap = self.path['band_2']
        out_ras = save_ls(self.path['band_qa'], equation, out_raster,
                          snap, mask_clouds)
        return out_ras

    def GNDVI(self, out_raster=None, mask_clouds=False):
        """
        Calculates GNDVI index

        Parameters
        ----------
            out_raster : str, optional
                Output filepath for calculated TIFF.
            mask_clouds : bool, optional
                Whether or not to apply cloud masking to output index with
                the QA band.

        Returns
        -------
            equation : array
                Output array of the generated index.

        """
        gdal.UseExceptions()
        gdal.AllRegister()
        np.seterr(divide='ignore', invalid='ignore')

        bands = self.load_bands(['band_5', 'band_3'])

        equation = ((bands["band_5"] - bands["band_3"])
                    / (bands["band_5"] + bands["band_3"]))

        snap = self.path['band_2']
        out_ras = save_ls(self.path['band_qa'], equation, out_raster,
                          snap, mask_clouds)
        return out_ras

    def SAVI(self, out_raster=None, soil_brightness=0.5, mask_clouds=False):
        """
        Calculates SAVI index

        Parameters
        ----------
            out_raster : str, optional
                Output filepath for calculated TIFF.
            soil_brightness : float
                Soil brightness factor to compute SAVI with. Defaults to 0.5
            mask_clouds : bool, optional
                Whether or not to apply cloud masking to output index with
                the QA band.

        Returns
        -------
            equation : array
                Output array of the generated index.

        """
        gdal.UseExceptions()
        gdal.AllRegister()
        np.seterr(divide='ignore', invalid='ignore')

        bands = self.load_bands(['band_5', 'band_4'])

        equation = ((bands["band_5"] - bands["band_4"]) /
                    (bands["band_5"] + bands["band_4"] + soil_brightness)) \
                    * (1 + soil_brightness)

        snap = self.path['band_2']
        out_ras = save_ls(self.path['band_qa'], equation, out_raster,
                          snap, mask_clouds)

        return out_ras

    def ARVI(self, out_raster=None, mask_clouds=False):
        """
        Calculates ARVI index

        Parameters
        ----------
            out_raster : str, optional
                Output filepath for calculated TIFF.
            mask_clouds : bool, optional
                Whether or not to apply cloud masking to output index with
                the QA band.

        Returns
        -------
            equation : array
                Output array of the generated index.

        """
        gdal.UseExceptions()
        gdal.AllRegister()
        np.seterr(divide='ignore', invalid='ignore')

        bands = self.load_bands(['band_2', 'band_4', 'band_5'])

        equation = ((bands["band_5"] - (2 * bands["band_4"]) + bands[
            "band_2"]) /
                    (bands["band_5"] + (2 * bands["band_4"]) + bands["band_2"]))

        snap = self.path['band_2']
        out_ras = save_ls(self.path['band_qa'], equation, out_raster,
                          snap, mask_clouds)

        return out_ras

    def VARI(self, out_raster=None, mask_clouds=False):
        """
        Calculates VARI index

        Parameters
        ----------
            out_raster : str, optional
                Output filepath for calculated TIFF.
            mask_clouds : bool, optional
                Whether or not to apply cloud masking to output index with
                the QA band.

        Returns
        -------
            equation : array
                Output array of the generated index.

        """
        gdal.UseExceptions()
        gdal.AllRegister()
        np.seterr(divide='ignore', invalid='ignore')

        bands = self.load_bands(['band_2', 'band_3', 'band_4'])

        equation = ((bands["band_3"] - bands["band_4"]) /
                    (bands["band_3"] + bands["band_4"] - bands["band_2"]))

        snap = self.path['band_2']
        out_ras = save_ls(self.path['band_qa'], equation, out_raster,
                          snap, mask_clouds)

        return out_ras

    def NDBI(self, out_raster=None, mask_clouds=False):
        """
        Calculates NDBI index

        Parameters
        ----------
            out_raster : str, optional
                Output filepath for calculated TIFF.
            mask_clouds : bool, optional
                Whether or not to apply cloud masking to output index with
                the QA band.

        Returns
        -------
            equation : array
                Output array of the generated index.

        """
        gdal.UseExceptions()
        gdal.AllRegister()
        np.seterr(divide='ignore', invalid='ignore')

        bands = self.load_bands(['band_5', 'band_6'])

        # Perform Calculation
        equation = ((bands["band_6"] - bands["band_5"]) / (
                    bands["band_6"] + bands["band_5"]))

        snap = self.path['band_2']
        out_ras = save_ls(self.path['band_qa'], equation, out_raster,
                          snap, mask_clouds)
        return out_ras

    def NDBaI(self, out_raster=None, mask_clouds=False):
        """
        Calculates NDBaI index

        Parameters
        ----------
            out_raster : str, optional
                Output filepath for calculated TIFF.
            mask_clouds : bool, optional
                Whether or not to apply cloud masking to output index with
                the QA band.

        Returns
        -------
            equation : array
                Output array of the generated index.

        """
        gdal.UseExceptions()
        gdal.AllRegister()
        np.seterr(divide='ignore', invalid='ignore')

        bands = self.load_bands(['band_6', 'band_10'])

        # Perform Calculation
        equation = ((bands["band_6"] - bands["band_10"]) /
                    (bands["band_6"] + bands["band_10"]))

        snap = self.path['band_2']
        out_ras = save_ls(self.path['band_qa'], equation, out_raster,
                          snap, mask_clouds)
        return out_ras

    def NBLI(self, out_raster=None, mask_clouds=False):
        """
        Calculates NBLI index

        Parameters
        ----------
            out_raster : str, optional
                Output filepath for calculated TIFF.
            mask_clouds : bool, optional
                Whether or not to apply cloud masking to output index with
                the QA band.

        Returns
        -------
            equation : array
                Output array of the generated index.

        """
        gdal.UseExceptions()
        gdal.AllRegister()
        np.seterr(divide='ignore', invalid='ignore')

        bands = self.load_bands(['band_4', 'band_10'])

        equation = ((bands["band_4"] - bands["band_10"]) /
                    (bands["band_4"] + bands["band_10"]))

        snap = self.path['band_2']
        out_ras = save_ls(self.path['band_qa'], equation, out_raster,
                          snap, mask_clouds)
        return out_ras

    def EBBI(self, out_raster=None, mask_clouds=False):
        """
        Calculates EBBI index

        Parameters
        ----------
            out_raster : str, optional
                Output filepath for calculated TIFF.
            mask_clouds : bool, optional
                Whether or not to apply cloud masking to output index with
                the QA band.

        Returns
        -------
            equation : array
                Output array of the generated index.

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

        snap = self.path['band_2']
        out_ras = save_ls(self.path['band_qa'], ebbi_mask, out_raster,
                          snap, mask_clouds)
        return out_ras

    def UI(self, out_raster=None, mask_clouds=False):
        """
        Calculates UI index

        Parameters
        ----------
            out_raster : str, optional
                Output filepath for calculated TIFF.
            mask_clouds : bool, optional
                Whether or not to apply cloud masking to output index with
                the QA band.

        Returns
        -------
            equation : array
                Output array of the generated index.

        """
        gdal.UseExceptions()
        gdal.AllRegister()
        np.seterr(divide='ignore', invalid='ignore')

        bands = self.load_bands(['band_5', 'band_7'])

        # Perform Calculation
        equation = ((bands["band_7"] - bands["band_5"]) /
                    (bands["band_7"] + bands["band_5"]))

        snap = self.path['band_2']
        out_ras = save_ls(self.path['band_qa'], equation, out_raster,
                          snap, mask_clouds)
        return out_ras

    def NBRI(self, out_raster=None, mask_clouds=False):
        """
        Calculates NBRI index

        Parameters
        ----------
            out_raster : str, optional
                Output filepath for calculated TIFF.
            mask_clouds : bool, optional
                Whether or not to apply cloud masking to output index with
                the QA band.

        Returns
        -------
            equation : array
                Output array of the generated index.

        """
        gdal.UseExceptions()
        gdal.AllRegister()
        np.seterr(divide='ignore', invalid='ignore')

        bands = self.load_bands(['band_5', 'band_7'])

        # calculation
        equation = ((bands["band_5"] - bands["band_7"]) /
                    (bands["band_5"] + bands["band_7"]))

        snap = self.path['band_2']
        out_ras = save_ls(self.path['band_qa'], equation, out_raster,
                          snap, mask_clouds)
        return out_ras

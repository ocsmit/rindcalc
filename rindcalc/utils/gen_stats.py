from osgeo import gdal
import numpy as np


def gen_stats(raster_path):
    """
    Prints minimum, maximum, mean, median, and standard deviation values for
    a raster.

    Parameters
    ----------
        raster_path : str, required
            input raster with which to generate statistical summary of.

    Returns
    -------
        minimum
        maximum
        mean
        median
        standard deviation
    """

    path = gdal.Open(raster_path)
    input_arr = path.GetRasterBand(1).ReadAsArray().astype(np.float32)

    arr_min = np.nanmin(input_arr)
    arr_max = np.nanmax(input_arr)
    arr_mean = np.nanmean(input_arr)
    arr_med = np.nanmedian(input_arr)
    arr_std = np.nanstd(input_arr)
    print('min: ' + str(arr_min),
          'max: ' + str(arr_max),
          'mean: ' + str(arr_mean),
          'med: ' + str(arr_med),
          'std: ' + str(arr_std))
    return arr_min, arr_max, arr_mean, arr_med, arr_std

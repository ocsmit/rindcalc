import numpy as np
from osgeo import gdal


def resample(band, cell_size, out=None):
    """
    Utility function to resample a raster and output it as either an
    array or TIFF

    Parameters
    ----------
        band : str
            Path to raster file to resample
        cell_size : int
            New size of the cells
        out: str, optional
            Filename to save the output TIFF

    Returns:
        resampled array

    """

    vrt = gdal.Translate('/vsimem/mem.vrt', band, xRes=cell_size, yRes=cell_size,
                         format='VRT')
    ds = gdal.Open('/vsimem/mem.vrt')
    array = ds.ReadAsArray().astype(np.float32)

    gdal.Unlink('/vsimem/mem.vrt')

    if out is not None:
        trans = gdal.Translate(out, vrt, format='GTiff')

    return array
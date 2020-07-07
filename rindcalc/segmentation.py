import numpy as np
from osgeo import gdal
from skimage.segmentation import felzenszwalb, quickshift
from rindcalc.utils.band_utils import save_index

def felzenszwalb_seg(input_index, output_raster=None, scale=1, sigma=0.8,
                     min_size=20):
        data = gdal.Open(input_index)
        arr = data.GetRasterBand(1).ReadAsArray().astype(np.float32)

        fz = felzenszwalb(arr, scale, sigma, min_size)
        if output_raster:
            save_index(fz, output_raster, snap=data, dType=gdal.GDT_Int16)
            return fz
        if not output_raster:
            return fz


def quickshift_seg(input_index, output_raster=None, ratio=1.0, kernel_size=5,
                   max_dist=10, return_tree=False, sigma=0, convert2lab=True,
                   random_seed=42):

    data = gdal.Open(input_index)
    arr = data.GetRasterBand(1).ReadAsArray().astype(np.float32)

    seg = quickshift(arr, ratio, kernel_size, max_dist, return_tree, sigma,
                     convert2lab, random_seed)
    if output_raster:
        save_index(seg, output_raster, snap=data, dType=gdal.GDT_Int16)
        return seg
    if not output_raster:
        return seg

###############################################################################
# Name: rindcalc.class_utils.py
# Author: Owen Smith, University of North Georgia IESA
# Purpose: Unsupervised classification function for rindcalcs
###############################################################################

import os
import numpy as np
from osgeo import gdal
from sklearn.cluster import MiniBatchKMeans


def k_means(input_raster, out_raster, clusters, itr, batch_size):

    # open input raster with gdal
    in_raster_path = gdal.Open(input_raster)
    raster = in_raster_path.GetRasterBand(1).ReadAsArray().astype(np.float32)
    snap = gdal.Open(input_raster)
    print("Raster read")

    # Mask raster to eliminate nan values
    np.seterr(divide='ignore', invalid='ignore')
    raster[np.isnan(raster)] = 0
    raster_mask = np.ma.MaskedArray(raster, mask=(raster == np.median))
    raster_mask.reshape(raster.shape)
    print("nan values masked")

    # K means clustering
    X = raster_mask.reshape((-1, 1))
    kcluster = MiniBatchKMeans(n_clusters=clusters, max_iter=itr, batch_size=batch_size)
    _ = kcluster.fit(X)
    raster_clustered = np.reshape(kcluster.labels_, raster.shape)
    print("Saving output")
    if os.path.exists(out_raster):
        raise IOError('Raster already exists')
    if not os.path.exists(out_raster):
        driver = gdal.GetDriverByName('GTiff')
        metadata = driver.GetMetadata()
        shape = raster_clustered.shape
        dst_ds = driver.Create(out_raster, xsize=shape[1], ysize=shape[0], bands=1, eType=gdal.GDT_Float32)
        proj = snap.GetProjection()
        geo = snap.GetGeoTransform()
        dst_ds.SetGeoTransform(geo)
        dst_ds.SetProjection(proj)
        dst_ds.GetRasterBand(1).WriteArray(raster_clustered)
        dst_ds.FlushCache()
        dst_ds = None

    return raster_clustered, print('K Means complete')

def NDMI_Index(landsat_dir, ndmi_out):
    # Create list with file names
    nir = glob(landsat_dir + "/*B5.tif")
    swir1 = glob(landsat_dir + "/*B6.tif")

    # Open with gdal & create numpy arrays
    gdal.UseExceptions()
    gdal.AllRegister()
    np.seterr(divide='ignore', invalid='ignore')
    NIR_path = gdal.Open(os.path.join(landsat_dir, nir[0]))
    nir_band = NIR_path.GetRasterBand(1).ReadAsArray().astype(np.float32)
    SWIR1_path = gdal.Open(os.path.join(landsat_dir, swir1[0]))
    swir1_band = SWIR1_path.GetRasterBand(1).ReadAsArray().astype(np.float32)
    snap = gdal.Open(os.path.join(landsat_dir, nir[0]))

    # calculation
    ndmi = ((nir_band - swir1_band) / (nir_band + swir1_band))

    # Save Raster
    if os.path.exists(ndmi_out):
        raise IOError('NDMI raster already created')
    if not os.path.exists(ndmi_out):
        driver = gdal.GetDriverByName('GTiff')
        metadata = driver.GetMetadata()
        shape = ndmi.shape
        dst_ds = driver.Create(ndmi_out, xsize=shape[1], ysize=shape[0], bands=1, eType=gdal.GDT_Float32)
        proj = snap.GetProjection()
        geo = snap.GetGeoTransform()
        dst_ds.SetGeoTransform(geo)
        dst_ds.SetProjection(proj)
        dst_ds.GetRasterBand(1).WriteArray(ndmi)
        dst_ds.FlushCache()
        dst_ds = None

    return print('ndmi created.')

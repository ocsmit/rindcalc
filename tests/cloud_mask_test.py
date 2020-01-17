import rindcalc as rc
import time

start_time = time.time()
landsat_dir = 'C:/Imagery/Landsat_8/aoi'
landsat_dir1 = 'C:/Imagery/Landsat_8/2020_01_15_cloud'
ndvi_out = 'C:/tmp/NDVI_nomask.tif'


rc.NDVI(landsat_dir1, ndvi_out, False)
end_time = time.time() - start_time
print(end_time / 60)
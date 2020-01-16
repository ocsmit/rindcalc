import rindcalc
import time

start_time = time.time()
landsat_dir = 'C:/Imagery/Landsat_8/2019_11_28'
landsat_dir1 = 'C:/Imagery/Landsat_8/2020_01_07_AUS'
landsat_dir2 = 'C:/Imagery/Landsat_8/2018_08_19'
input_raster = 'C:/Research/ALCC_RE/out/AWEIsh_unmasked.tif'
out_raster = 'C:/tmp/NDVI.tif'

rindcalc.NDVI(landsat_dir2, out_raster)
end_time = time.time() - start_time
print(end_time / 60)


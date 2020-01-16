import os
import numpy as np
from osgeo import gdal
from glob import glob


def cloud_mask(landsat_dir, out):
    # Get qa path
    qa = glob(landsat_dri + "/*BQA.tif")

    # Read band with gdal
    gdal.UseExceptions()
    gdal.AllRegister()
    np.seterr(divide='ignore', invalid='ignore')

    qa_path = gdal.Open(os.path.join(landsat_dir, qa[0])
    qa_band = qa_path.GetRasterBand(1).ReadAsArray().astype(np.float32)

    # Change cloud values to 0 everything else to 1
    cloud_med = [2752, 2756, 2760, 2764, 3008, 3012, 3016, 3020, 
				 3776, 3780, 3784, 3788, 6848, 6852, 6856, 6860,
				 7104, 7108, 7112, 7116, 7876, 7880, 7884]
	cloud_hi = [2800, 2804, 2808, 2812, 6896, 6900, 6904, 6908]
	cloud = [2976, 2980, 2984, 2988, 3008, 3012, 3016, 3020, 
				7072, 7076, 7080, 7084, 7104, 7108, 7112, 7116]				
                
    np.seterr(divide='ignore', invalid='ignore')
	
	m = np.ma.array(test, 
		mask=np.logical_or.reduce([test == value for value in 
		[2976, 2980, 2984, 2988, 3008, 3012, 3016, 3020, 2]]))
	np.ma.set_fill_value(m, 0)
	m1 = m.filled()
	m1[m1 != 0] = 1
	
	for i in range(len(cloud):
		test1 = np.where((test == i), 0, 1))
    raster[(raster)] = 0
    raster_mask = np.ma.MaskedArray(raster, mask=(raster == np.median))
    raster_mask.reshape(raster.shape)
	
    

# Rindcalc 
**A Spectral Index Raster Calculator**

[![Documentation Status](https://readthedocs.org/projects/rindcalc/badge/?version=latest)](https://rindcalc.readthedocs.io/en/latest/?badge=latest)

Rindcalc is an open source python library built on numpy and gdal aiming to
provide seamless and accurate raster index calculations and composites of 
Landsat-8 imagery using gdal and numpy.    

It currently consists of index calculation and utility functions for Landsat
-8 and USDA NAIP imagery, with Sentinel-2 and MODIS satellite functions in
the work 

**Install with pip**

Dependencies:
 * GDAL - *need to build from .whl file* 
 * NumPy

```console
pip install rindcalc
```    

**Install with conda**

```console
conda install -c rindcalc rindcalc 
```
If rindcalc is not importing after conda install on Windows 10 then rindcalc 
files need to be moved from Lib/pythonX.X/site-packages/ to Lib/site-packages
within the conda env folder. 


### For more information visit the [Rindcalc documentation](https://rindcalc.readthedocs.io/en/latest/)

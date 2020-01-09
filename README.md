# rindcalc
Module created to allow for quick raster index calculation from Landsat-8 using gdal and numpy.   


Pulls .TIF files directly from Landsat-8 database with unedited file names. 

If file names have been changed simply edit each function to pull proper bands.


## Indices

**Water**
- AWEIsh = ((Blue + 2.5 * Green - 1.5 * (NIR + SWIR1) - 0.25 * SWIR2)) / (Blue + Green + NIR + SWIR1 + SWIR2)

- NDMI = ((NIR - SWIR1) / (NIR + SWIR1))

- MNDWI = ((Green - SWIR1) / (Green + SWIR1))

**Vegetation**
- NDVI = ((NIR - Red) / (NIR + Red))
    
- SAVI = ((NIR - Red) / (NIR + Red + L)) x (1 + L) 
    - *L = Soil Brightness Factor*

**Landscape**
- NDBI = (SWIR1 - NIR) / (SWIR1 + NIR)

- NDBaI = ((SWIR1 - TIR) / (SWIR1 + TIR))

- NBLI = ((Red - TIR) / (Red + TIR))

- EBBI = ((swir1_band - nir_band) / (10 * (np.sqrt(swir1_band + tir_band))))


## Dependencies
> * GDAL (v 3.0.0 or greater)
> * numpy (v 1.0.0 or greater)
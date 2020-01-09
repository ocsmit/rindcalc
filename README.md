# rindcalc
Module created to allow for quick raster index calculation from Landsat-8 using gdal and numpy.   
Pulls .TIF files directly from Landsat-8 database with unedited file names. If file names have been changed simply edit each function to pull proper bands.

## Dependencies
> * GDAL (v 3.0.0 or greater)
> * numpy (v 1.0.0 or greater)



## Modules


> landsat_dir = Landsat-8 folder that contains all bands
> 
>*_out = out file raster will be saved as

i.e. Landsat-8 folder structure:
>LC08_L1TP_091086_20191222_20191223_01_RT
>
>|-- LC08_L1TP_091086_20191222_20191223_01_RT_B1.TIF
>
>|-- LC08_L1TP_091086_20191222_20191223_01_RT_B2.TIF
>
>|-- LC08_L1TP_091086_20191222_20191223_01_RT_B3.TIF


* AWEIsh_Index(landsat_dir, aweish_out)
* NDMI_Index(landsat_dir, ndmi_out)
* MNDWI_Index(landsat_dir, mndwi_out)
* NDVI_Index(landsat_dir, ndvi_out)
* SAVI_Index(landsat_dir, soil_brightness, savi_out)
* NDBI_Index(landsat_dir, ndbi_out)
* NDBaI_Index(landsat_dir, ndbai_out)
* NBLI_Index(landsat_dir, nbli_out)
* EBBI_Index(landsat_dir, ebbi_out)


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

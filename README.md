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
```textmate
.
|--LC08_L1TP_091086_20191222_20191223_01_RT
|   |-- LC08_L1TP_091086_20191222_20191223_01_RT_B1.TIF
|   |-- LC08_L1TP_091086_20191222_20191223_01_RT_B2.TIF
|   |-- LC08_L1TP_091086_20191222_20191223_01_RT_B3.TIF
|   |-- ...
|-- 2019_12_22
|   |-- LC08_L1TP_091086_20191222_20191223_01_RT_B1.TIF
|   |-- LC08_L1TP_091086_20191222_20191223_01_RT_B2.TIF
|   |-- LC08_L1TP_091086_20191222_20191223_01_RT_B3.TIF
|   |-- ...
```


* AWEIsh(landsat_dir, aweish_out)
* NDMI(landsat_dir, ndmi_out)
* MNDWI(landsat_dir, mndwi_out)
* NDVI(landsat_dir, ndvi_out)
* SAVI(landsat_dir, soil_brightness, savi_out)
* NDBI(landsat_dir, ndbi_out)
* NDBaI(landsat_dir, ndbai_out)
* NBLI(landsat_dir, nbli_out)
* EBBI(landsat_dir, ebbi_out)
* NBRI(landsat_dir, nbri_out)

EX:

```python
import rindcalc as rc
landsat_dir = 'C:/.../.../LC08_L1TP_091086_20191222_20191223_01_RT'
ndvi_out = 'C:/.../.../NDVI_1.tif'
rc.NDVI(landsat_dir, ndvi_out)
```
OR:

```python
import rindcalc as rc
rc.NDVI(landsat_dir = 'C:/.../.../2019_12_22', ndvi_out = 'C:/.../.../NDVI_2.tif')
```

## Indices

**Water**
- AWEIsh = ((Blue + 2.5 * Green - 1.5 * (NIR + SWIR1) - 0.25 * SWIR2)) / (Blue + Green + NIR + SWIR1 + SWIR2)

- NDWI = ((nir_band - swir1_band) / (nir_band + swir1_band))

- MNDWI = ((Green - SWIR1) / (Green + SWIR1))

**Moisture**

- NDMI = ((NIR - SWIR1) / (NIR + SWIR1))

**Vegetation**
- NDVI = ((NIR - Red) / (NIR + Red))
    
- SAVI = ((NIR - Red) / (NIR + Red + L)) x (1 + L) 
    - *L = Soil Brightness Factor*

**Landscape**
- NDBI = (SWIR1 - NIR) / (SWIR1 + NIR)

- NDBaI = ((SWIR1 - TIR) / (SWIR1 + TIR))

- NBLI = ((Red - TIR) / (Red + TIR))

- EBBI = ((swir1_band - nir_band) / (10 * (np.sqrt(swir1_band + tir_band))))

**Fire**

- NBRI = ((nir_band - swir2_band) / (nir_band + swir2_band))

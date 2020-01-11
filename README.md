# rindcalc
**Raster Index Calculator**


rind calc is a python package created to allow complete raster index calculation using Landsat-8 using gdal and numpy.
Landsat bands are pulled directly from file downloaded from USGS containing all bands os landsat scene. 
Since rindcalc only requires the file in which Landsat-8 bands are contained instead of each individual 
band to be specified, it allows for easy, quick, and seamless index calculations from Landsat-8 imagery.   

## Dependencies
> * GDAL (v 3.0.0 or greater)
> * numpy (v 1.0.0 or greater)

## Installation 
**Windows**

>pip install rindcalc

For Windows installation [gdal](https://pypi.org/project/GDAL/) wheels must be installed first.

## Modules


> landsat_dir = Landsat-8 folder that contains all bands
> 
>*_out = out file raster will be saved as

i.e. Landsat-8 folder structure:
```textmate
.
|--LC08_L1TP_091086_20191222_20191223_01_RT                     Landsat Folder ex. #1
|   |-- LC08_L1TP_091086_20191222_20191223_01_RT_B1.TIF
|   |-- LC08_L1TP_091086_20191222_20191223_01_RT_B2.TIF
|   |-- LC08_L1TP_091086_20191222_20191223_01_RT_B3.TIF
|   |-- ...
|-- 2019_12_22                                                  Landsat Folder ex. #2
|   |-- LC08_L1TP_091086_20191222_20191223_01_RT_B1.TIF
|   |-- LC08_L1TP_091086_20191222_20191223_01_RT_B2.TIF
|   |-- LC08_L1TP_091086_20191222_20191223_01_RT_B3.TIF
|   |-- ...
```

* AWEIsh(landsat_dir, aweish_out)
* NDMI(landsat_dir, ndmi_out)
* MNDWI(landsat_dir, mndwi_out)
* NDVI(landsat_dir, ndvi_out)
* GNDVI(landsat_dir)
* SAVI(landsat_dir, soil_brightness, savi_out)
* NDBI(landsat_dir, ndbi_out)
* NDBaI(landsat_dir, ndbai_out)
* NBLI(landsat_dir, nbli_out)
* EBBI(landsat_dir, ebbi_out)
* UI(landsat_dir, ui_out )
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

- Green NDVI (GNDVI) = ((nir_band - green_band) / (nir_band + green_band))
    
- SAVI = ((NIR - Red) / (NIR + Red + L)) x (1 + L) 
    - *L = Soil Brightness Factor*

**Urban/Landscape**
- NDBI = (SWIR1 - NIR) / (SWIR1 + NIR)

- NDBaI = ((SWIR1 - TIR) / (SWIR1 + TIR))

- NBLI = ((Red - TIR) / (Red + TIR))

- EBBI = ((swir1_band - nir_band) / (10 * (np.sqrt(swir1_band + tir_band))))

- UI = ((swir2_band - nir_band) / (swir2_band + nir_band))

**Fire**

- NBRI = ((nir_band - swir2_band) / (nir_band + swir2_band))

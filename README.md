# rindcalc 
**Raster Index Calculator**

v.1.2.6 notes: Increased stability when reading input landsat bands.

rindcalc is an open source python library built on numpy and gdal aiming to
provide seamless and accurate raster index calculations and composites of 
Landsat-8 imagery using gdal and numpy. Landsat bands are pulled directly
from files downloaded from USGS containing all bands in the landsat scene
. Since rindcalc uses the standard naming convention of landsat bands, it
only needs the folder in which Landsat-8 bands are contained instead. This
method allows for easy, quick, and consistent index calculations from Landsat
-8 imagery.   

Indices: AWEIsh, AWEInsh, NDMI, MNDWI, NDVI, GNDVI, SAVI, NDBI, NDBaI, 
         NBLI, EBBI, UI, NBRI,

Composites: RGB, False Color

Unsupervised Classification: K-Means (Mini Batch)

The k-means unsupervised classification module utilizes sci-kit learn's
MiniBatchKMeans which provides significantly faster computation times than
the standard K-means algorithm, but with slightly worse result 
[[1]](https://scikit-learn.org/stable/modules/clustering.html#mini-batch-kmeans).
'No Data' values are populated with the median value of the array as the
classification algorithm does not work with numpy arrays that contain 'nan' 
values.


## Dependencies
> * GDAL (v 3.0.0 or greater)
> * numpy (v 1.0.0 or greater)
> * sci-kit learn (v0.22.1 or greater)

## Installation 
**Windows**

>pip install rindcalc

For Windows installation [gdal](https://pypi.org/project/GDAL/) 
wheels must be installed first.

## Modules

**Composite Modules | rindcalc.composite_utils**
* RGB(landsat_dir, out_composite)
* FalseColor(landsat_dir, out_composite)

**Index Modules | rindcalc.index_utils**
* AWEIsh(landsat_dir, aweish_out, mask_clouds)
* AWEInsh(landsat_dir, aweinsh_out, mask_clouds)
* NDMI(landsat_dir, ndmi_out)
* MNDWI(landsat_dir, mndwi_out)
* NDVI(landsat_dir, ndvi_out, mask_clouds)
* GNDVI(landsat_dir, gndvi_out)
* ARVI(landsat_dir, arvi_out)
* VARI(landsat_dir, vari_out)
* SAVI(landsat_dir, soil_brightness, savi_out)
* NDBI(landsat_dir, ndbi_out)
* NDBaI(landsat_dir, ndbai_out)
* NBLI(landsat_dir, nbli_out)
* EBBI(landsat_dir, ebbi_out)
* UI(landsat_dir, ui_out )
* NBRI(landsat_dir, nbri_out)

> landsat_dir = Landsat-8 folder that contains all bands
> 
>*_out = out file raster will be saved as
>
>mask_clouds = True or False

i.e. Landsat-8 folder structure:
```textmate
.
|--LC08_L1TP_091086_20191222_20191223_01_RT               Landsat Folder ex. #1
|   |-- LC08_L1TP_091086_20191222_20191223_01_RT_B1.TIF
|   |-- LC08_L1TP_091086_20191222_20191223_01_RT_B2.TIF
|   |-- LC08_L1TP_091086_20191222_20191223_01_RT_B3.TIF
|   |-- ...
|-- 2019_12_22                                            Landsat Folder ex. #2
|   |-- LC08_L1TP_091086_20191222_20191223_01_RT_B1.TIF
|   |-- LC08_L1TP_091086_20191222_20191223_01_RT_B2.TIF
|   |-- LC08_L1TP_091086_20191222_20191223_01_RT_B3.TIF
|   |-- ...
```

**K Means Classification Module | rindcalc.class_utils**

* k_means(input_raster, out_raster, clusters, itr, batch_size)
> clusters = Number of classes wanted

> itr = Number of iterations to perform

> batch_size = Size of mini batches

Example:

```python
import rindcalc as rc
landsat_dir = './.../LC08_L1TP_091086_20191222_20191223_01_RT'
ndvi_out = './.../NDVI_1.tif'
rc.NDVI(landsat_dir, ndvi_out, False)
```
OR:

```python
import rindcalc as rc
rc.NDVI(landsat_dir = './.../2019_12_22', ndvi_out = './.../NDVI_2.tif'
, mask_clouds=True)
```

K means unsupervised example:
```python
import rindcalc as rc
input_raster = 'C:/.../.../NDVI.tif'
out_raster = 'C:/.../.../NDVI_K.TIF'
clusters = 2
itr = 10
batch_size = 50
rc.k_means(input_raster, out_raster, clusters, itr, batch_size)
```

## Landsat-8 Bands


| Band Number      |     Name    | µm   | Resolution   |
| ------------- |:-------------:| -----:|-----:|
| 1| Coastal/Aerosal| 0.433-0.453 |30 m|
| 2| Blue           | 0.450-0.515 |30 m |
| 3| Green          | 0.525-0.600 |30 m |
| 4| Red            | 0.630-0.680 |30 m |
| 5| NIR            | 0.845-0.885 |30 m |
| 6| SWIR 1         | 1.560-1.660 |30 m |
| 7| SWIR 2         | 2.100-2.300 |30 m |
| 8| Panchromatic   | 0.500-0.680 |15 m |
| 9| Cirrus         | 1.360-1.390 |30 m |
| 10| TIR 1         | 10.6-11.2   |100 m |
| 11| TIR 2         | 11.5-12.5   |100 m |

## Cloud Masking Algorithm

Cloud masking takes the landsat QA band and reads it as a numpy array.
 Values classed as clouds and cloud shadows are then given the value of 0.
Values not equal to zero are then given the value of 1. This mask array is
then reshaped back into it's original dimensons. The reshaped array is then
multiplied by each input band of  the index calulation. This ensures all
pixels where clouds and cloud shadows are contained are replaced with 'nan
' and all other pixels retain their original values.

```textmate
mask_values = [2800, 2804, 2808, 2812, 6986, 6900, 6904, 6908,
               2976, 2980, 2984, 2988, 3008, 3012, 3016, 3020,
               7072, 7076, 7080, 7084, 7104, 7108, 7112, 7116]

m = np.ma.array(qa_band,
                    mask=np.logical_or.reduce([qa_band == value for value 
                                                in mask_values]))
np.ma.set_fill_value(m, 0)
m1 = m.filled()
m1[m1 != 0] = 1

m1.reshape(qa_band.shape)
```

## Indices

**Composites**
RGB = (Red, Green, Blue)

**Water**
- AWEIsh = ((Blue + 2.5 * Green - 1.5 * (NIR + SWIR1) - 0.25 * SWIR2)) / 
              (Blue + Green + NIR + SWIR1 + SWIR2) [1]

- AWEInsh = ((4 * (green_band - swir1_band) - (0.25 * nir_band + 2.75 * 
                swir1_band)) /  (green_band + swir1_band + nir_band)) [1]

- MNDWI = ((Green - SWIR1) / (Green + SWIR1))  [3]

**Moisture**

- NDMI = ((NIR - SWIR1) / (NIR + SWIR1)) [2]

**Vegetation**
- NDVI = ((NIR - Red) / (NIR + Red)) [4]

- Green NDVI (GNDVI) = ((nir_band - green_band) / (nir_band + green_band)) 
    
- ARVI = ((nir_band - (2 * red_band) + blue_band) 
            / (nir_band + (2 * red_band) + blue_band)) [5]

- VARI = ((green_band - red_band) / (green_band + red_band - blue_band))
    
- SAVI = ((NIR - Red) / (NIR + Red + L)) x (1 + L) 
    - *L = Soil Brightness Factor*
- MSAVI2 = (((2 * nir_band + 1) - (np.sqrt(((2 * nir_band + 1)**2) - 8 * 
            (nir_band - red_band)))) / 2)

**Urban/Landscape**
- NDBI = (SWIR1 - NIR) / (SWIR1 + NIR)

- NDBaI = ((SWIR1 - TIR) / (SWIR1 + TIR))

- NBLI = ((Red - TIR) / (Red + TIR))

- EBBI = ((swir1_band - nir_band) / (10 * (np.sqrt(swir1_band + tir_band))))

- UI = ((swir2_band - nir_band) / (swir2_band + nir_band))

**Fire**

- NBRI = ((nir_band - swir2_band) / (nir_band + swir2_band))


### References
[1] Feyisa, G. L., Meilby, H., Fensholt, R., & Proud, S. R. (2014).
    Automated Water Extraction Index: A new technique for surface water mapping
    using Landsat imagery. Remote Sensing of Environment, 140, 23-35

[2] Gao, B. C. (1996). NDWI—A normalized difference water index for remote
    sensing of vegetation liquid water from space. Remote sensing of
    environment, 58(3), 257-266.

[3] Xu, H. (2006). Modification of normalised difference water index (NDWI
    ) to enhance open water features in remotely sensed imagery. International
    journal of remote sensing, 27(14), 3025-3033.

[4] Tucker, C. J. (1979). Red and photographic infrared linear combinations
    for monitoring vegetation. Remote sensing of Environment, 8(2), 127-150.

[5] Kaufman, Y. J., & Tanre, D. (1992). Atmospherically resistant vegetation
    index (ARVI) for EOS-MODIS. IEEE transactions on Geoscience and Remote
    Sensing, 30(2), 261-270.
Landsat-8
=========

Landsat bands are pulled directly from files downloaded from USGS containing
all bands in the landsat scene. Since rindcalc uses the standard naming
convention of landsat bands, it only needs the folder in which Landsat-8
bands are contained instead. This method allows for easy, quick, and
consistent index calculations from Landsat-8 imagery.

Index Modules | rindcalc.ls.index_utils
---------------------------------------

**AWEIsh(landsat_dir, aweish_out, mask_clouds=False)**

    **Parameters:**

            **landsat_dir ::** *str, required*
                * Folder path where all landsat bands for the scene are contained.

            **aweish_out ::** *str, required*
                * Output path and file name for calculated index raster.

            **mask_clouds ::** *boolean, optional (default=False)*
                * Whether or not to apply cloud mask to scene based of QA band.

    **Example:**

            .. code-block:: python

               import rindcalc as rc
               landsat_dir = './.../LC08_L1TP_091086_20191222_20191223_01_RT'
               aweish_out = './.../AWEIsh_1.tif'
               rc.ls.AWEIsh(landsat_dir, aweish_out, False)

       **OR**

            .. code-block:: python

               import rindcalc as rc
               rc.NDVI('./.../2019_12_22', './.../AWEIsh_2.tif', True)


**AWEInsh(landsat_dir, aweinsh_out, mask_clouds=False)**

**NDMI(landsat_dir, ndmi_out)**

**MNDWI(landsat_dir, mndwi_out)**

**NDVI(landsat_dir, ndvi_out, mask_clouds=False)**

**GNDVI(landsat_dir, gndvi_out)**

**ARVI(landsat_dir, arvi_out)**

**VARI(landsat_dir, vari_out)**

**SAVI(landsat_dir, soil_brightness=0.5, savi_out)**

**NDBI(landsat_dir, ndbi_out)**

**NDBaI(landsat_dir, ndbai_out)**

**NBLI(landsat_dir, nbli_out)**

**EBBI(landsat_dir, ebbi_out)**

**UI(landsat_dir, ui_out)**

**NBRI(landsat_dir, nbri_out)**

Composite Modules | rindcalc.ls.composite_utils
-----------------------------------------------

**RGB(landsat_dir, out_composite)**

**FalseColor(landsat_dir, out_composite)**

Cloud Masking - Landsat-8
-------------------------

Cloud masking takes the landsat QA band and reads it as a numpy array.
Values classed as clouds and cloud shadows are then given the value of 0.
Values not equal to zero are then given the value of 1. This mask array is
then reshaped back into it's original dimensons. The reshaped array is then
multiplied by each input band of  the index calulation. This ensures all
pixels where clouds and cloud shadows are contained are replaced with 'nan'
and all other pixels retain their original values.

.. code-block:: python

   # Values that are clouds
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


Index Formulas
--------------

**Water**

- AWEIsh = ((Blue + 2.5 * Green - 1.5 * (NIR + SWIR1) - 0.25 *
                SWIR2)) /  (Blue + Green + NIR + SWIR1 + SWIR2)) [1]

- AWEInsh = ((4 * (Green - SWIR1) - (0.25 * NIR + 2.75 *
                SWIR1)) /  (Green + SWIR1 + NIR)) [1]

- MNDWI = ((Green - SWIR1) / (Green + SWIR1))  [3]

**Moisture**

- NDMI = ((NIR - SWIR1) / (NIR + SWIR1)) [2]

**Vegetation**

- NDVI = ((NIR - Red) / (NIR + Red)) [4]

- Green NDVI (GNDVI) = (( NIR - Green) / ( NIR + Green))

- ARVI = ((NIR - (2 * Red) + Blue)
            / (NIR + (2 * Red) + Blue)) [5]

- VARI = ((Green - Red) / (Green + Red - Blue))

- SAVI = ((NIR - Red) / (NIR + Red + L)) x (1 + L)
    - *L = Soil Brightness Factor*
- MSAVI2 = (((2 *  NIR   + 1) - (np.sqrt(((2 *  NIR   + 1)**2) - 8 *
            ( NIR   - Red  )))) / 2)

**Urban/Landscape**

- NDBI = (SWIR1 - NIR) / (SWIR1 + NIR)

- NDBaI = ((SWIR1 - TIR) / (SWIR1 + TIR))

- NBLI = ((Red - TIR) / (Red + TIR))

- EBBI = ((SWIR1 - NIR) / (10 * (np.sqrt(SWIR1 + tir))))

- UI = ((SWIR2 - NIR) / (SWIR2 + NIR))

**Fire**

- NBRI = ((NIR - SWIR2) / ( NIR + SWIR2))



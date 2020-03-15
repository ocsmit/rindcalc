Landsat-8 | rindcalc.ls
=======================

.. contents:: Contents
    :local:

Rindcalc uses the standard naming convention of landsat bands, it only needs
the folder in which Landsat-8 bands are contained as the input. This method
allowsfor easy, quick, and consistent index calculations from Landsat-8 imagery.


Index Modules | rindcalc.ls.indicies
-------------------------------------

Water Indices
^^^^^^^^^^^^^

**AWEIsh(landsat_dir, aweish_out, mask_clouds=False)**

    Calculates the Automated Water Extraction Index (shadow) with Landsat-8
    and outputs a TIFF raster file.

    AWEIsh = (Blue + 2.5 * Green - 1.5 * (NIR + SWIR1) - 0.25 *
                SWIR2) /  (Blue + Green + NIR + SWIR1 + SWIR2)

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
               rc.ls.AWEInsh('./.../LC08_L1TP_091086_20191222_20191223_01_RT',
                             './.../AWEIsh.tif',
                              True)


**AWEInsh(landsat_dir, aweinsh_out, mask_clouds=False)**

    Calculates the Automated Water Extraction Index (no shadow) with Landsat-8
    and outputs a TIFF raster file.

    AWEInsh = (4 * (Green - SWIR1) - (0.25 * NIR + 2.75 *
                SWIR1)) /  (Green + SWIR1 + NIR)

    **Parameters:**

            **landsat_dir ::** *str, required*
                * Folder path where all landsat bands for the scene are contained.

            **aweinsh_out ::** *str, required*
                * Output path and file name for calculated index raster.

            **mask_clouds ::** *boolean, optional (default=False)*
                * Whether or not to apply cloud mask to scene based of QA band.

    **Example:**

            .. code-block:: python

               import rindcalc as rc
               rc.ls.AWEInsh('./.../LC08_L1TP_091086_20191222_20191223_01_RT',
                             './.../AWEInsh.tif',
                              True)


**NDMI(landsat_dir, ndmi_out)**

    Calculates the Normalized Difference Moisture Index with Landsat-8
    and outputs a TIFF raster file.

    NDMI = (NIR - SWIR1) / (NIR + SWIR1)

    **Parameters:**

            **landsat_dir ::** *str, required*
                * Folder path where all landsat bands for the scene are contained.

            **ndmi_out ::** *str, required*
                * Output path and file name for calculated index raster.

    **Example:**

            .. code-block:: python

               import rindcalc as rc
               rc.ls.NDMI('./.../LC08_L1TP_091086_20191222_20191223_01_RT',
                          './.../NDMI.tif')

**MNDWI(landsat_dir, mndwi_out)**

    Calculates the Modified Normalized Difference Water Index with Landsat-8
    and outputs a TIFF raster file.

    MNDWI = (Green - SWIR1) / (Green + SWIR1)

    **Parameters:**

            **landsat_dir ::** *str, required*
                * Folder path where all landsat bands for the scene are contained.

            **mndwi_out ::** *str, required*
                * Output path and file name for calculated index raster.

    **Example:**

            .. code-block:: python

               import rindcalc as rc
               rc.ls.MNDWI('./.../LC08_L1TP_091086_20191222_20191223_01_RT',
                           './.../NDMI.tif')

Vegetation Indices
^^^^^^^^^^^^^^^^^^

**NDVI(landsat_dir, ndvi_out, mask_clouds=False)**

    Calculates the Normalized Difference Vegetation Index with Landsat-8
    and outputs a TIFF raster file.

    NDVI = ((NIR - Red) / (NIR + Red))

    **Parameters:**

            **landsat_dir ::** *str, required*
                * Folder path where all landsat bands for the scene are contained.

            **ndvi_out ::** *str, required*
                * Output path and file name for calculated index raster.

            **mask_clouds ::** *boolean, optional (default=False)*
                * Whether or not to apply cloud mask to scene based of QA band.

    **Example:**

            .. code-block:: python

               import rindcalc as rc
               rc.ls.NDVI('./.../LC08_L1TP_091086_20191222_20191223_01_RT',
                          './.../NDVI.tif',
                          True)

**GNDVI(landsat_dir, gndvi_out)**

    Calculates the Green Normalized Difference Vegetation Index with Landsat-8
    and outputs a TIFF raster file.

    GNDVI = (NIR - Green) / (NIR + Green)

    **Parameters:**

            **landsat_dir ::** *str, required*
                * Folder path where all landsat bands for the scene are contained.

            **gndvi_out ::** *str, required*
                * Output path and file name for calculated index raster.

    **Example:**

            .. code-block:: python

               import rindcalc as rc
               rc.ls.GNDVI('./.../LC08_L1TP_091086_20191222_20191223_01_RT',
                          './.../GNDVI.tif')

**ARVI(landsat_dir, arvi_out)**

    Calculates the Atmospherically Resistant Vegetation Index with Landsat-8
    and outputs a TIFF raster file.

    ARVI = (NIR - (2 * Red) + Blue) / (NIR + (2 * Red) + Blue)

    **Parameters:**

            **landsat_dir ::** *str, required*
                * Folder path where all landsat bands for the scene are contained.

            **arvi_out ::** *str, required*
                * Output path and file name for calculated index raster.

    **Example:**

            .. code-block:: python

               import rindcalc as rc
               rc.ls.ARVI('./.../LC08_L1TP_091086_20191222_20191223_01_RT',
                          './.../ARVI.tif')

**VARI(landsat_dir, vari_out)**

    Calculates the Visual Atmospherically Resistant Index with Landsat-8
    and outputs a TIFF raster file.

    VARI = ((Green - Red) / (Green + Red - Blue))

    **Parameters:**

            **landsat_dir ::** *str, required*
                * Folder path where all landsat bands for the scene are contained.

            **vari_out ::** *str, required*
                * Output path and file name for calculated index raster.

    **Example:**

            .. code-block:: python

               import rindcalc as rc
               rc.ls.VARI('./.../LC08_L1TP_091086_20191222_20191223_01_RT',
                          './.../VARI.tif')

**SAVI(landsat_dir, soil_brightness=0.5, savi_out)**

    Calculates the Soil Adjusted Vegetation Index with Landsat-8
    and outputs a TIFF raster file.

    SAVI = ((NIR - Red) / (NIR + Red + L)) x (1 + L)
                                        *L = Soil BrightnessFactor*

    **Parameters:**

            **landsat_dir ::** *str, required*
                * Folder path where all landsat bands for the scene are contained.

            **soil_brightness ::** *float, required (default=0.5)*

            **savi_out ::** *str, required*
                * Output path and file name for calculated index raster.

    **Example:**

            .. code-block:: python

               import rindcalc as rc
               rc.ls.SAVI('./.../LC08_L1TP_091086_20191222_20191223_01_RT',
                          0.75,
                          './.../SAVI.tif')

Urban / Landscape Indices
^^^^^^^^^^^^^^^^^^^^^^^^^

**NDBI(landsat_dir, ndbi_out)**

    Calculates the Normalized Difference Built-up Index with Landsat-8
    and outputs a TIFF raster file.

    NDBI = (SWIR1 - NIR) / (SWIR1 + NIR)

    **Parameters:**

            **landsat_dir ::** *str, required*
                * Folder path where all landsat bands for the scene are contained.

            **ndbi_out ::** *str, required*
                * Output path and file name for calculated index raster.

    **Example:**

            .. code-block:: python

               import rindcalc as rc
               rc.ls.NDBI('./.../LC08_L1TP_091086_20191222_20191223_01_RT',
                          './.../NDBI.tif')

**NDBaI(landsat_dir, ndbai_out)**

    Calculates the Normalized Difference Bareness Index with Landsat-8
    and outputs a TIFF raster file.

    NDBaI = ((SWIR1 - TIR) / (SWIR1 + TIR))

    **Parameters:**

            **landsat_dir ::** *str, required*
                * Folder path where all landsat bands for the scene are contained.

            **ndbai_out ::** *str, required*
                * Output path and file name for calculated index raster.

    **Example:**

            .. code-block:: python

               import rindcalc as rc
               rc.ls.NDBaI('./.../LC08_L1TP_091086_20191222_20191223_01_RT',
                          './.../NDBaI.tif')

**NBLI(landsat_dir, nbli_out)**

    Calculates the Normalized Bare Land Index with Landsat-8
    and outputs a TIFF raster file.

    NBLI = (Red - TIR) / (Red + TIR)

    **Parameters:**

            **landsat_dir ::** *str, required*
                * Folder path where all landsat bands for the scene are contained.

            **nbli_out ::** *str, required*
                * Output path and file name for calculated index raster.

    **Example:**

            .. code-block:: python

               import rindcalc as rc
               rc.ls.NBLI('./.../LC08_L1TP_091086_20191222_20191223_01_RT',
                          './.../NBLI.tif')


**EBBI(landsat_dir, ebbi_out)**

    Calculates the Enhanced Built-up and Bareness Index with Landsat-8
    and outputs a TIFF raster file.

    EBBI = (SWIR1 - NIR) / (10 * (sqrt(SWIR1 + tir)))

    **Parameters:**

            **landsat_dir ::** *str, required*
                * Folder path where all landsat bands for the scene are contained.

            **ebbi_out ::** *str, required*
                * Output path and file name for calculated index raster.

    **Example:**

            .. code-block:: python

               import rindcalc as rc
               rc.ls.EBBI('./.../LC08_L1TP_091086_20191222_20191223_01_RT',
                          './.../EBBI.tif')


**UI(landsat_dir, ui_out)**

    Calculates the Urban Index with Landsat-8 and outputs a TIFF raster file.

    UI = (SWIR2 - NIR) / (SWIR2 + NIR)

    **Parameters:**

            **landsat_dir ::** *str, required*
                * Folder path where all landsat bands for the scene are contained.

            **ui_out ::** *str, required*
                * Output path and file name for calculated index raster.

    **Example:**

            .. code-block:: python

               import rindcalc as rc
               rc.ls.UI('./.../LC08_L1TP_091086_20191222_20191223_01_RT',
                          './.../UI.tif')

Burn / Fire Indices
^^^^^^^^^^^^^^^^^^^

**NBRI(landsat_dir, nbri_out)**

    Calculates the Normalized Burn Ratio Index with Landsat-8 and outputs a
    TIFF raster file.

    UI = (SWIR2 - NIR) / (SWIR2 + NIR)

    **Parameters:**

            **landsat_dir ::** *str, required*
                * Folder path where all landsat bands for the scene are contained.

            **nbri_out ::** *str, required*
                * Output path and file name for calculated index raster.

    **Example:**

            .. code-block:: python

               import rindcalc as rc
               rc.ls.NBRI('./.../LC08_L1TP_091086_20191222_20191223_01_RT',
                          './.../NBRI.tif')

Composite Modules | rindcalc.ls.composites
------------------------------------------

RGB Composite
^^^^^^^^^^^^^

**RGB(landsat_dir, out_composite)**

    Creates a RGB composite using Landsat-8 and out puts a TIFF raster file
    with the values normalized between 0 - 255

    **Parameters:**

            **landsat_dir ::** *str, required*
                * Folder path where all landsat bands for the scene are contained.

            **out_composite ::** *str, required*
                * Output path and file name for calculated index raster.

    **Example:**

            .. code-block:: python

               import rindcalc as rc
               rc.ls.RGB('./.../LC08_L1TP_091086_20191222_20191223_01_RT',
                          './.../RGB_Composite.tif')

False Color Composite
^^^^^^^^^^^^^^^^^^^^^

**FalseColor(landsat_dir, out_composite)**

    Creates a False Color composite using Landsat-8 and out puts a TIFF raster
    file with the values normalized between 0 - 255

    **Parameters:**

            **landsat_dir ::** *str, required*
                * Folder path where all landsat bands for the scene are contained.

            **out_composite ::** *str, required*
                * Output path and file name for calculated index raster.

    **Example:**

            .. code-block:: python

               import rindcalc as rc
               rc.ls.FalseColor('./.../LC08_L1TP_091086_20191222_20191223_01_RT',
                          './.../False_Color_Composite.tif')

Cloud Masking - Landsat-8 | rindcalc.ls.cloud_masking
-----------------------------------------------------

Cloud masking takes the landsat QA band and reads it as a numpy array.
Values classed as clouds and cloud shadows are then given the value of 0.
Values not equal to zero are then given the value of 1. This mask array is
then reshaped back into it's original dimensions. The reshaped array is then
multiplied by each input band of  the index calculation. This ensures all
pixels where clouds and cloud shadows are contained are replaced with 'nan'
and all other pixels retain their original values.

Cloud mask Process:

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

Band Utilities | rindcalc.ls.band_utils
---------------------------------------

Utility functions for use with other rindcalc functions or analysis

**save_raster(in_array, out, snap, dType=gdal.GDT_Float32)**

    Saves the input NumPy array as a one band raster.

    **Parameters:**

            **in_array ::** *array, required*
                * NumPy array to be saved as TIFF raster file.

            **out ::** *str, required*
                * Output path and file name for TIFF raster file.

            **snap ::** *gdal raster, required*
                * Raster file with which projections and geotransformations
                  are based off.

            **dType ::** *gdal datatype, required (default=gdal.GDT_Float32)*
                * Datatype to save raster as.

**gen_stats(raster_path)**

    Prints minimum, maximum, mean, median, and standard deviation values for
    a raster.

    **Parameters:**

            **raster_path ::** *str, required*
                * input raster with which to generate statistical summary of.

    **Returns:**

            **minimum, maximum, mean, median, standard deviation**


Index Modules | rindcalc.ls.indices
===================================

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

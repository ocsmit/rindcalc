Index Modules | rindcalc.naip.indices
=====================================

calculate_all(in_naip, our_dir):
--------------------------------------------------------
    Calculates all indices in rindcalc.naip.indices for NAIP image and outputs
    into a specified output folder with the output file names being the name of
    the function. i.e: NDVI.tif

    **Parameters:**

            **in_naip :: str, required**
                * File path for NAIP image.

             **out_dir :: str, required**
                * File path of output directory.

    **Example:**

            .. code-block:: python

               from rindcalc import naip
               naip.calculate_all('./.../m_3008101_ne_17_1_20151017.tif',
                          './.../3008101_ne_17_indices')


Vegetation Indices
^^^^^^^^^^^^^^^^^^

ARVI(in_naip, arvi_out)
--------------------------------------------------------
    Calculates the Atmospherically Resistant Vegetation Index with NAIP Imagery
    and outputs a TIFF raster file.

    ARVI = (NIR - (2 * Red) + Blue) / (NIR + (2 * Red) + Blue)

    **Parameters:**

            **in_naip ::** *str, required*
                * File path for NAIP image.

            **arvi_out ::** *str, required*
                * Output path and file name for calculated index raster.

    **Example:**

            .. code-block:: python

               from rindcalc import naip
               naip.ARVI('./.../m_3008101_ne_17_1_20151017.tif',
                          './.../ARVI.tif')

VARI(in_naip, vari_out)
--------------------------------------------------------
    Calculates the Visual Atmospherically Resistant Index with NAIP Imagery
    and outputs a TIFF raster file.

    VARI = ((Green - Red) / (Green + Red - Blue))

    **Parameters:**

            **in_naip ::** *str, required*
                * File path for NAIP image.

            **vari_out ::** *str, required*
                * Output path and file name for calculated index raster.

    **Example:**

            .. code-block:: python

               from rindcalc import naip
               naip.VARI('./.../m_3008101_ne_17_1_20151017.tif',
                          './.../VARI.tif')

nVARI(in_naip, nvari_out)
--------------------------------------------------------
    Calculates the Visual Atmospherically Resistant Index with NAIP Imagery
    and outputs a TIFF raster file.

    **Normalized between -1 - 1**

    nVARI = ((Green - Red) / (Green + Red - Blue))

    **Parameters:**

            **in_naip ::** *str, required*
                * File path for NAIP image.

            **nvari_out ::** *str, required*
                * Output path and file name for calculated index raster.

    **Example:**

            .. code-block:: python

               from rindcalc import naip
               naip.nVARI('./.../m_3008101_ne_17_1_20151017.tif',
                          './.../nVARI.tif')

NDVI(in_naip, ndvi_out)
--------------------------------------------------------
    Calculates the Normalized Difference Vegetation Index with NAIP imagery
    and outputs a TIFF raster file.

    NDVI = ((NIR - Red) / (NIR + Red))

    **Parameters:**

            **in_naip ::** *str, required*
                * File path for NAIP image.

            **ndvi_out ::** *str, required*
                * Output path and file name for calculated index raster.

    **Example:**

            .. code-block:: python

               from rindcalc import naip
               naip.NDVI('./.../m_3008101_ne_17_1_20151017.tif',
                          './.../NDVI.tif')

SAVI(in_naip, soil_brightness=0.5, savi_out)
--------------------------------------------------------
    Calculates the Soil Adjusted Vegetation Index with NAIP imagery
    and outputs a TIFF raster file.

    SAVI = ((NIR - Red) / (NIR + Red + L)) x (1 + L)
                                        *L = Soil BrightnessFactor*

    **Parameters:**

             **in_naip ::** *str, required*
                * File path for NAIP image.

            **savi_out ::** *str, required*
                * Output path and file name for calculated index raster.

            **soil_brightness ::** *float, required (default=0.5)*

    **Example:**

            .. code-block:: python

               from rindcalc import naip
               naip.SAVI('./.../m_3008101_ne_17_1_20151017.tif',
                          './.../SAVI.tif')

RedRatio(in_naip, redratio_out)
----------------------------------

    Calculates red band ratio with NAIP imagery
    and outputs a TIFF raster file.

    RedRatio(in_naip, soil_brightness=0.5, savi_out)

    Calculates the Soil Adjusted Vegetation Index with NAIP imagery
    and outputs a TIFF raster file.

    ratio = (blue_band + red_band + green_band) / red_band

    **Parameters:**

            in_naip :: str, required
                * File path for NAIP image.

            redratio_out :: str, required
                * Output path and file name for calculated index raster.

    **Example:**

            .. code-block:: python

               from rindcalc import naip
               naip.RedRatio('./.../m_3008101_ne_17_1_20151017.tif',
                          './.../Red_Ratio.tif')
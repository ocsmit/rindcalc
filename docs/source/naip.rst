NAIP | rindcalc.naip
====================

.. contents:: Contents
    :local:


Index Modules | rindcalc.naip.indices
-------------------------------------

Vegetation Indices
^^^^^^^^^^^^^^^^^^

**ARVI(in_naip, arvi_out)**

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

               import rindcalc as rc
               rc.naip.ARVI('./.../m_3008101_ne_17_1_20151017.tif',
                          './.../ARVI.tif')

**VARI(in_naip, vari_out)**

    Calculates the Visual Atmospherically Resistant Index with NAIP Imagery
    and outputs a TIFF raster file.

    VARI = ((Green - Red) / (Green + Red - Blue))

    **Parameters:**

            **in_naip ::** *str, required*
                * File path for NAIP image.

            **vari_out ::** *str, required*
                * Output path and file name for calculated index raster.

**nVARI(in_naip, nvari_out)**

    Calculates the Visual Atmospherically Resistant Index with NAIP Imagery
    and outputs a TIFF raster file.

    **Normalized between -1 - 1**

    nVARI = ((Green - Red) / (Green + Red - Blue))

    **Parameters:**

            **in_naip ::** *str, required*
                * File path for NAIP image.

            **nvari_out ::** *str, required*
                * Output path and file name for calculated index raster.

**NDVI(in_naip, ndvi_out)**

    Calculates the Normalized Difference Vegetation Index with NAIP imagery
    and outputs a TIFF raster file.

    NDVI = ((NIR - Red) / (NIR + Red))

    **Parameters:**

            **in_naip ::** *str, required*
                * File path for NAIP image.

            **ndvi_out ::** *str, required*
                * Output path and file name for calculated index raster.

**SAVI(in_naip, soil_brightness=0.5, savi_out)**

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


Band Utilities | rindcalc.naip.band_utils
-----------------------------------------

Utility functions for use with other rindcalc functions or analysis

**def norm(array, max_value, min_value)**

    Normalizes an input array to be between the input max and min values.

    **Parameters**

        **in_array ::** *array, required*
            * array to normalize.

        **max_value ::** *integer, required*
            * Max value for normalization

        **min_value ::** *integer, required*
            * Minimum value for normalization.

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
**Band Utilities | rindcalc.band_utils**
========================================

Utility functions for use with other rindcalc functions or analysis

def norm(array, max_value, min_value)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

    Normalizes an input array to be between the input max and min values.

    **Parameters**

        **in_array ::** *array, required*
            * array to normalize.

        **max_value ::** *integer, required*
            * Max value for normalization

        **min_value ::** *integer, required*
            * Minimum value for normalization.

save_raster(in_array, out, snap, dType=gdal.GDT_Float32)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
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

gen_stats(raster_path)
^^^^^^^^^^^^^^^^^^^^^^^^^^
    Prints minimum, maximum, mean, median, and standard deviation values for
    a raster.

    **Parameters:**

            **raster_path ::** *str, required*
                * input raster with which to generate statistical summary of.

    **Returns:**

            **minimum, maximum, mean, median, standard deviation**

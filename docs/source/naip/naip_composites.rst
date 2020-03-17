False Color Composite
^^^^^^^^^^^^^^^^^^^^^

FalseColor(landsat_dir, out_composite)
---------------------------------------
    Creates a False Color composite using NAIP imagery and outputs a TIFF
    raster file with the values normalized between 0 - 255

    **Parameters:**

            **in_naip ::** *str, required*
                * File path for NAIP image.

            **out_composite ::** *str, required*
                * Output path and file name for calculated index raster.

    **Example:**

            .. code-block:: python

               import rindcalc as rc
               rc.naip.FalseColor('./.../m_3008101_ne_17_1_20151017.tif',
                          './.../NAIP_False_Color.tif')
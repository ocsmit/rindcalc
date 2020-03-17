Composite Modules | rindcalc.ls.composites
==========================================

**RGB Composite**
^^^^^^^^^^^^^^^^^

RGB(landsat_dir, out_composite)
------------------------------------------------
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

**False Color Composite**
^^^^^^^^^^^^^^^^^^^^^^^^^

FalseColor(landsat_dir, out_composite)
------------------------------------------------
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
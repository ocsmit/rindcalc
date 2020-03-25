**Rindcalc Documentation**
==========================

About
---------
Rindcalc is an open source python library built on NumPy and GDAL with the
goal of providing seamless raster index calculations and
composites of satellite imagery for remote sensing. It looks to fill the gap
left by proprietary softwares and open source initiatives alike when it comes
to the need to create and process spectral index raster files.


Satellites & Imagery
------------------------
 * Landsat-8
    * Index raster creation
    * Composites
    * Cloud Masking
 * National Agricultural Imagery Program - NAIP
    * Index raster creation
    * Composites
 * Sentinel-2 - WIP
 * MODIS - WIP

**Example of use:**
-------------------

Calculating the ARVI of a NAIP tile and saving as a raster.

.. code-block:: python

   import rindcalc as rc

   # set inputs and outputs
   input_naip = '/naip_folder/m_3008101_ne_17_1_20151017.tif'
   output_arvi = '/naip_outputs/ARVI_3008101_ne_17.tif'

   rc.naip.ARVI(input_naip, output_ndvi)


Output ARVI raster:
    .. image:: https://user-images.githubusercontent.com/55674113/76912798-82a7cf80-688b-11ea-9117-20e9e34f8999.png
       :alt: ARVI output
       :width: 502px
       :height: 574.7px


Creating a false color composite of a Landsat-8 Scene.

.. code-block:: python

   import rindcalc as rc

   rc.ls.FalseColor('/landsat_8/LC08_L1TP_197031_20131212_20170428_01_T1',
                      '/landsat_8_outputs/FalseColor_Barcelona.tif')


Output false color composite:
    .. image:: https://user-images.githubusercontent.com/55674113/77016121-2c02ca00-694d-11ea-9131-06836238e7fb.png
       :alt: False color composite output
       :width: 772.8px
       :height: 824px



--------------------------------------------------------------------------------

.. toctree::
   :caption: Contents
   :maxdepth: 1

   install
   landsat/Landsat-8
   naip/naip
   band_utils
   Index Formula List
   Contact


:Authors: Owen Smith, University of North Georgia IESA
:Version: 2.0.2
:License: GPL v3.0

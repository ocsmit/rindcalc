**Rindcalc Documentation**
==========================
About
---------
Rindcalc is an open source python library built on numpy and gdal with the
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
       :width: 410px
       :height: 515px


Creating a false color composite of a NAIP tile.

.. code-block:: python

   import rindcalc as rc

   rc.naip.FalseColor('/naip_folder/m_3008101_ne_17_1_20151017.tif',
                      '/naip_outputs/FC_3008101_ne_17.tif')


Output false color composite:
    .. image:: https://user-images.githubusercontent.com/55674113/76913678-18445e80-688e-11ea-844d-c53c12c22850.png
       :alt: False color composite output
       :width: 410px
       :height: 515px



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
:Version: 2.0.0
:License: GPL v3.0

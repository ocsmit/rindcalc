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
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: python

   import rindcalc as rc

   # set inputs and outputs
   input_naip = '/naip_folder/m_3008101_ne_17_1_20151017.tif'
   output_arvi = '/naip_outputs/ARVI_3008101_ne_17.tif'

   data = rc.NAIP(path)
   data.ARVI(output_ndvi)


Output ARVI raster:
    .. image:: https://user-images.githubusercontent.com/55674113/76912798-82a7cf80-688b-11ea-9117-20e9e34f8999.png
       :alt: ARVI output
       :width: 502px
       :height: 574.7px


Using in conjunction with matplotlib
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: python

   import rindcalc as rc
   import matplotlib.pyplot as plt

   ls = '/landsat_8/2019_11_28'
   index = ls.AWEIsh('/landsat_8/2019_11_28')
   plt.imshow(index, 'ocean')
   plt.title('AWEIsh - Water Index')
   plt.show()

.. image:: https://user-images.githubusercontent.com/55674113/80848987-4930e680-8be3-11ea-9564-a1fabd9c32e8.png
   :alt: False color composite output


Creating a false color composite of a Landsat-8 Scene.
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: python

   from rindcalc import Landsat

   ls = rc.Landsat('/landsat_8/LC08_L1TP_197031_20131212_20170428_01_T1')
   ls.composite(['band_5', 'band_4', 'band_3'], '/landsat_8_outputs/FalseColor_Barcelona.tif')


Output false color composite:
    .. image:: https://user-images.githubusercontent.com/55674113/77016121-2c02ca00-694d-11ea-9131-06836238e7fb.png
       :alt: False color composite output
       :width: 390px
       :height: 412px

Install
-------------------------------------

With pip from PyPI repository
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

`PyPI repository <https://pypi.org/project/rindcalc/>`_

Dependencies
 * GDAL (v 3.0.0 or greater)
 * NumPy (v 1.0.0 or greater)

.. code-block:: python

   pip install rindcalc

With Conda from Anaconda Cloud
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

`Conda Cloud <https://anaconda.org/rindcalc/rindcalc>`_

.. code-block:: python

   conda install -c rindcalc rindcalc


Latest development version
^^^^^^^^^^^^^^^^^^^^^^^^^^

For latest version clone the `Rindcalc GitHub Repository <https://github.com/ocsmit/rindcalc>`_
and add the module to path with sys.path.append.



--------------------------------------------------------------------------------

.. toctree::
   :caption: Contents
   :maxdepth: 1

   Landsat-8
   naip
   sent
   band_utils
   Index Formula List
   Contact


:Authors: Owen Smith, University of North Georgia IESA
:Version: 2.0.5
:License: GPL v3.0

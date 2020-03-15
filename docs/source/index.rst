Rindcalc Documentation
======================
A remote sensing index calculation library

Directory
---------

.. toctree::
   :maxdepth: 2

   Landsat-8
   naip
   Index Formula List
   Contact

About
-----
Rindcalc is an open source python library built on numpy and gdal with the
goal of providing seamless raster index calculations and
composites of satellite imagery for remote sensing

Satellites & Imagery
--------------------
 * Landsat-8
 * National Agricultural Imagery Program - NAIP
 * Sentinel-2 - WIP
 * MODIS - WIP

Installation
------------
Install with pip from PyPI repository:

Dependencies
 * GDAL (v 3.0.0 or greater)
 * NumPy (v 1.0.0 or greater)

.. code-block:: python

   pip install rindcalc

Install with conda

.. code-block:: python

   conda install -c rindcalc rindcalc

--------------------------------------------------------------------------------

:Authors: Owen Smith, University of North Georgia IESA
:Version: 2.0.0
:License: GPL v3.0

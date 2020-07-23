**Landsat-8 | rindcalc.ls**
===========================

Rindcalc uses the standard naming convention of landsat bands, it only needs
the folder in which Landsat-8 bands are contained as the input. This method
allows for easy, quick, and consistent index calculations from Landsat-8
imagery.

The Landsat 8 satellite orbits the the Earth in a sun-synchronous, near-polar
orbit, at an altitude of 705 km (438 mi), inclined at 98.2 degrees, and
circles the Earth every 99 minutes.  The satellite has a 16-day repeat cycle
with an equatorial crossing time: 10:00 a.m. +/- 15 minutes.

Landsat 8 aquires about 740 scenes a day on the Worldwide Reference System-2
(WRS-2) path/row system, with a swath overlap (or sidelap) varying from 7
percent at the Equator to a maximum of approximately 85 percent at extreme
latitudes. The scene size is 185 km x 180 km (114 mi x 112 mi) `(USGS)
<https://www.usgs.gov/land-resources/nli/landsat/landsat-8?qt-science_support_page_related_con=0#qt-science_support_page_related_con>`_.

.. figure:: https://user-images.githubusercontent.com/55674113/77010453-29e63e80-6940-11ea-943e-2fe6f0da21b6.png
   :alt: Landsat calculated with RGB composite

   Landsat-8 scene composite created with rindcalc RGB composite function.

--------------------------------------------------------------------------------

.. toctree::
   :caption: Functions
   :maxdepth: 2

   ls_indices
   ls_composites
   cloud_mask
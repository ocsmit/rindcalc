Landsat-8 | rindcalc.ls
=======================

Rindcalc uses the standard naming convention of landsat bands, it only needs
the folder in which Landsat-8 bands are contained as the input. This method
allowsfor easy, quick, and consistent index calculations from Landsat-8 imagery.


.. toctree::
   :caption: Functions
   :maxdepth: 1

   ls_indices
   ls_composites


Cloud Masking - Landsat-8 | rindcalc.ls.cloud_masking
-----------------------------------------------------

Cloud masking takes the landsat QA band and reads it as a numpy array.
Values classed as clouds and cloud shadows are then given the value of 0.
Values not equal to zero are then given the value of 1. This mask array is
then reshaped back into it's original dimensions. The reshaped array is then
multiplied by each input band of  the index calculation. This ensures all
pixels where clouds and cloud shadows are contained are replaced with 'nan'
and all other pixels retain their original values.

Cloud mask Process:

.. code-block:: python

   # Values that are clouds
   mask_values = [2800, 2804, 2808, 2812, 6986, 6900, 6904, 6908,
                  2976, 2980, 2984, 2988, 3008, 3012, 3016, 3020,
                  7072, 7076, 7080, 7084, 7104, 7108, 7112, 7116]

   m = np.ma.array(qa_band,
                   mask=np.logical_or.reduce([qa_band == value for value
                                             in mask_values]))
   np.ma.set_fill_value(m, 0)
   m1 = m.filled()
   m1[m1 != 0] = 1

   m1.reshape(qa_band.shape)

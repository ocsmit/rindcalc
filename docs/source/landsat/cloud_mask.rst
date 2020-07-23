Cloud Masking Method - Landsat-8 | rindcalc.ls.cloud_masking
============================================================

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


Example:

.. figure:: https://user-images.githubusercontent.com/55674113/77011807-0c66a400-6943-11ea-8610-4af6b5a99fb6.png
   :alt: Cloud Mask NDVI
   :width: 772.8px
   :height: 824px

   NDVI with cloud mask applied.


.. figure:: https://user-images.githubusercontent.com/55674113/77011948-56e82080-6943-11ea-8025-010ef7c32844.png
   :alt: No Cloud Mask NDVI
   :width: 772.8px
   :height: 824px

   NDVI with cloud mask not applied with same color values.
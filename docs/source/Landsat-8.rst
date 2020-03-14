Modules
=======
Contains all modules

---------------------

Satellites & Imagery
^^^^^^^^^^^^^^^^^^^^
 * Landsat-8
 * National Agricultural Imagery Program - NAIP
 * Sentinel-2 - WIP
 * MODIS - WIP

Landsat-8
=========

Composite Modules | rindcalc.composite_utils
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
 * RGB(landsat_dir, out_composite)
 * FalseColor(landsat_dir, out_composite)

Index Modules | rindcalc.index_utils
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
 * AWEIsh(landsat_dir, aweish_out, mask_clouds)
 * AWEInsh(landsat_dir, aweinsh_out, mask_clouds)
 * NDMI(landsat_dir, ndmi_out)
 * MNDWI(landsat_dir, mndwi_out)
 * NDVI(landsat_dir, ndvi_out, mask_clouds)
 * GNDVI(landsat_dir, gndvi_out)
 * ARVI(landsat_dir, arvi_out)
 * VARI(landsat_dir, vari_out)
 * SAVI(landsat_dir, soil_brightness, savi_out)
 * NDBI(landsat_dir, ndbi_out)
 * NDBaI(landsat_dir, ndbai_out)
 * NBLI(landsat_dir, nbli_out)
 * EBBI(landsat_dir, ebbi_out)
 * UI(landsat_dir, ui_out )
 * NBRI(landsat_dir, nbri_out)
**Index Formula List**
######################

All index formulas are grouped by specific use here.

--------------------------------------------------------------------------------

**Water Indices**
==================

Indices designed for water detection

Automated Water Extraction Index | AWEIsh
-----------------------------------------
- For areas with increased shadow.
- AWEIsh = ((Blue + 2.5 * Green - 1.5 * (NIR + SWIR1) - 0.25 * SWIR2)) /
            (Blue + Green + NIR + SWIR1 + SWIR2))

Automated Water Extraction Index | AWEInsh
------------------------------------------
- For areas with minimal shadow.
- AWEInsh = ((4 * (Green - SWIR1) - (0.25 * NIR + 2.75 *
                SWIR1)) /  (Green + SWIR1 + NIR))

Normalized Difference Moisture Index | NDMI
-------------------------------------------
- NDMI = ((NIR - SWIR1) / (NIR + SWIR1))

Modified Normalized Difference Water Index | MNDWI
--------------------------------------------------
- MNDWI = ((Green - SWIR1) / (Green + SWIR1))

--------------------------------------------------------------------------------

**Vegetation Indices**
======================

Indices designed for vegetation detection

Normalized Difference Vegetation Index | NDVI
---------------------------------------------
- NDVI = (NIR - Red) / (NIR + Red)

Green Normalized Difference Vegetation Index | GNDVI
----------------------------------------------------
- GNDVI = ( NIR - Green) / ( NIR + Green)

Atmospherically Resistant Vegetation Index | ARVI
-------------------------------------------------
- ARVI = (NIR - (2 * Red) + Blue) / (NIR + (2 * Red) + Blue)

Visual Atmospherically Resistant Index | VARI
---------------------------------------------
- VARI = ((Green - Red) / (Green + Red - Blue))

Soil Adjusted Vegetation Index | SAVI
-------------------------------------
- SAVI = ((NIR - Red) / (NIR + Red + L)) x (1 + L)
    - *L = Soil Brightness Factor*

Structure Insensitive Pigment Index | SIPI
------------------------------------------
- SIPI = (NIR – Blue) / (NIR – Red)


--------------------------------------------------------------------------------

**Urban / Landscape Indices**
=============================
Indices designed for urban and landscape detection


Normalized Difference Built-up Index | NDBI
-------------------------------------------
- NDBI = (SWIR1 - NIR) / (SWIR1 + NIR)

Nomrmalized Difference Bareness Index | NDBaI
---------------------------------------------
- NDBaI = ((SWIR1 - TIR) / (SWIR1 + TIR))

Normalized Bare Land Index | NBLI
---------------------------------
- NBLI = ((Red - TIR) / (Red + TIR))

Enhanced Built-up and Barness Index | EBBI
------------------------------------------
- EBBI = ((SWIR1 - NIR) / (10 * (np.sqrt(SWIR1 + tir))))

Urban Index | UI
----------------
- UI = ((SWIR2 - NIR) / (SWIR2 + NIR))

--------------------------------------------------------------------------------

**Burn / Fire Indices**
=======================

Indices designed for fire and burned area detection

Normalized Burn Ratio Index | NBRI
----------------------------------
- NBRI = ((NIR - SWIR2) / ( NIR + SWIR2))



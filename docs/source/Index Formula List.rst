Index Formula List
==================

Water Indices
^^^^^^^^^^^^^

- AWEIsh = ((Blue + 2.5 * Green - 1.5 * (NIR + SWIR1) - 0.25 *
                SWIR2)) /  (Blue + Green + NIR + SWIR1 + SWIR2))

- AWEInsh = ((4 * (Green - SWIR1) - (0.25 * NIR + 2.75 *
                SWIR1)) /  (Green + SWIR1 + NIR))

- NDMI = ((NIR - SWIR1) / (NIR + SWIR1))

- MNDWI = ((Green - SWIR1) / (Green + SWIR1))

Vegetation Indices
^^^^^^^^^^^^^^^^^^

- NDVI = ((NIR - Red) / (NIR + Red)) [4]

- Green NDVI (GNDVI) = (( NIR - Green) / ( NIR + Green))

- ARVI = ((NIR - (2 * Red) + Blue)
            / (NIR + (2 * Red) + Blue)) [5]

- VARI = ((Green - Red) / (Green + Red - Blue))

- SAVI = ((NIR - Red) / (NIR + Red + L)) x (1 + L)
    - *L = Soil Brightness Factor*
- MSAVI2 = (((2 *  NIR   + 1) - (np.sqrt(((2 *  NIR   + 1)**2) - 8 *
            ( NIR   - Red  )))) / 2)

Urban / Landscape Indices
^^^^^^^^^^^^^^^^^^^^^^^^^

- NDBI = (SWIR1 - NIR) / (SWIR1 + NIR)

- NDBaI = ((SWIR1 - TIR) / (SWIR1 + TIR))

- NBLI = ((Red - TIR) / (Red + TIR))

- EBBI = ((SWIR1 - NIR) / (10 * (np.sqrt(SWIR1 + tir))))

- UI = ((SWIR2 - NIR) / (SWIR2 + NIR))

Burn / Fire Indices
^^^^^^^^^^^^^^^^^^^

- NBRI = ((NIR - SWIR2) / ( NIR + SWIR2))



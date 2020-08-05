---
title: 'Rindcalc: A Python Package For Remote Sensing Calculations and Manipulation.'
tags:
  - Python
  - GIS
  - Remote Sensing
  - Satellite Imagery
authors:
  - name: Owen C. Smith
    orcid: 0000-0002-4740-2985
    affiliation: 1
affiliations:
 - name: Undergrad, University of North Georgia IESA.
   index: 1
date: 25 May 2020
bibliography: paper.bib
---

# Summary 
The public availability of multispectral satellite imagery combined with the high temporal frequency with which it is taken allows for imagery to be incorporated into many aspects of research.
The uses of indices from remote sensing products range from tracking vegetation health, monitoring forest canopy, observing water levels, fire detection, and even aiding in the creation of land cover datasets [@Silleos:2006; @Joshi:2006; @Ghulam:2007; @Roy:2006; @Jin:2013].
Indices are computed through the application of algebraic formulas where the inputs are either the spectral bands or other ancillary information from multispectral imagery.
However, outside of raster calculator GUI's, like those in proprietary geospatial software’s such as ArcGIS and ERDAS, and in the open source QGIS, there is currently no streamlined method for calculating these indices.
Additionally, other processing functions are provided such as compositing and cell size resampling.

The goal of Rindcalc is to provide an efficient and seamless processing toolbox for capable of working directly with remote sensing products outside of a GUI or the us of a complex python pipeline from scratch.
The indices created with Rindcalc can subsequently be added to other workflows and algorithms to aid in research.

# Methodology
Rindcalc is seperated by remote sensing product with functionality for Landsat-8, Sentinel-2, and NAIP imagery provided at the time of writing.
For each remote sensing product a class is intitialized which will read the filepath of each raster band utilizing the default naming conventions of each product.
The classes are further seperated into key methods to effiecently process imagery.


![Simple overveiw of the Rindcalc python library](fig-rindcalc.png)

# Mathematics

Single dollars ($) are required for inline mathematics e.g. $f(x) = e^{\pi/x}$

Double dollars make self-standing equations:

$$\Theta(x) = \left\{\begin{array}{l}
0\textrm{ if } x < 0\cr
1\textrm{ else}
\end{array}\right.$$

You can also use plain \LaTeX for equations
\begin{equation}\label{eq:fourier}
\hat f(\omega) = \int_{-\infty}^{\infty} f(x) e^{i\omega x} dx
\end{equation}
and refer to \autoref{eq:fourier} from text.

# Citations

Citations to entries in paper.bib should be in
[rMarkdown](http://rmarkdown.rstudio.com/authoring_bibliographies_and_citations.html)
format.

If you want to cite a software repository URL (e.g. something on GitHub without a preferred
citation) then you can do it with the example BibTeX entry below for @fidgit.

For a quick reference, the following citation commands can be used:
- `@author:2001`  ->  "Author et al. (2001)"
- `[@author:2001]` -> "(Author et al., 2001)"
- `[@author1:2001; @author2:2001]` -> "(Author1 et al., 2001; Author2 et al., 2002)"

# Figures

Figures can be included like this:
![Caption for example figure.\label{fig:example}](figure.png)
and referenced from text using \autoref{fig:example}.

Fenced code blocks are rendered with syntax highlighting:
```python
for n in range(10):
    yield f(n)
```	

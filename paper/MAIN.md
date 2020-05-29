---
title: 'Rindcalc: A Python package for remote sensing calculations and manipulation.'
tags:
  - Python
  - GIS
  - remote sensing
  - satellite imagery
authors:
  - name: Owen C. Smith
    affiliation: 1
affiliations:
 - name: Undergrad, University of North Georgia IESA.
   index: 1
date: 25 May 2020
bibliography: paper.bib
---

# Summary 
The public availability of multispectral satellite imagery combined with the high temporal frequency it which it is taken makes it highly suitable for use in research, especially its use in the creation of spectral indices which are hugely important in any type of environmental monitoring.
Its uses range from tracking vegetation health, monitoring forest canopy, observing water levels, fire detection, and even aiding in the creation of landcover datasets (Silleos et al. 2006, Joshi et al. 2006, Ghulam et al. 2006, Roy et al. 2006, Jin et al. 2013).
To create and process these indices, the image bands are read as a matrix of cells with each cell containing value, called a raster dataset.
Raster datasets allow for algebraic formulas to be calculated using the different bands from multispectral imagery.
 However, outside of proprietary cumbersome raster calculators, like those in expensive geospatial software’s such as ArcGIS and ERDAS there is currently no streamlined method for calculating these indices.
 The lack of utility combine with high costs leads to the use of Python coding.
 There are a few open source spectral image processing Python modules, most notably Spectral Python [Spy] and HyperSpy , but while they offer robust image processing functions there is still no efficient method function for the creation of spectral indices (de la Peña et al. 2019, Boggs 2019).
 The lack of efficient functions can hinder any process that requires the use of spectral indices, whether it be for research or everyday use as it requires one to set up their own Python scripts for automation. 
The proposed library looks to address the lack of dedicated index functions by creating an efficient open source Python library that will allow for easy index creation. 


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

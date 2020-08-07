# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [3.0.0] - 2020-08-6

### Added
  
  - Full Sentinel-2 support 
  - Added resampling function

### Changed

  - Complete restructuring of the code base. 
  - Individual classes created for Sentinel-2, Landsat-8, & NAIP.
  - Update structure for reading data, new dictionary classes to allow for the 
    easy integration with other python libraries.
  
## [2.0.5] - 2020-05-01

### Changed 

- Make saving output indices optional to increase post calculation matplotlib 
  and NumPy functionality.

- Update documentation to new theme / bring formating into line across documentation.

[Unreleased]: https://github.com/ocsmit/rindcalc/compare/2.0.5...master
[2.0.5]: https://github.com/ocsmit/rindcalc/compare/2.0.4...2.0.5

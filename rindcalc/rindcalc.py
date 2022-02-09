from typing import List, Union, Dict
import json
from pathlib import Path
from dataclasses import dataclass


# External imports
import numpy as np
from osgeo import gdal

# Type aliases
RindcalcDir = Dict[str, Union[str, Path]]


BAND_MAP = "./band_mappings.json"
INDEX_MAP = "./index_map.json"


@dataclass
class RDir:
    blue: Union[str, None]
    cirrus: Union[str, None]
    coastal_aerosol: Union[str, None]
    green: Union[str, None]
    nir_broad: Union[str, None]
    nir_narrow: Union[str, None]
    red: Union[str, None]
    red_edge_1: Union[str, None]
    red_edge_2: Union[str, None]
    red_edge_3: Union[str, None]
    swir_1: Union[str, None]
    swir_2: Union[str, None]
    thermal_1: Union[str, None]
    thermal_2: Union[str, None]
    water_vapor: Union[str, None]
    parent: Union[Path]

    def full_path(self, band):
        return self.parent / getattr(self, band)


def parse_names(files: List[str], parent_dir: Path, sensor="LC08") -> RindcalcDir:
    """
    docstring
    """

    with open(BAND_MAP) as f:
        band_map = json.load(f)

    band_map.pop("__source", None)

    out_files = {}
    for key, item in band_map.items():
        match = [item.get(sensor) in s for s in files]
        out_files[key] = files[match.index(True)] if any(match) else None

    out_files["parent"] = parent_dir

    return out_files


def get_files(directory: Union[Path, str]) -> Union[List[str], Path]:
    files = []
    for path in Path(directory).iterdir():
        if path.is_file():
            files.append(path.name)
        parent = path.parent

    return files, parent


def open_raster(files: RindcalcDir, band):
    src_path = files.get("parent") / files.get(band)
    if not src_path.exists:
        raise Exception(f"{src_path} does not exist")

    src = gdal.Open(str(src_path))
    return src


def get_band(src: gdal.Dataset, idx: int = 1) -> np.ndarray:
    return src.GetRasterBand(idx).ReadAsArray()


#####

t, parent_dir = get_files("/Users/osmith2/Data/HLS/S30")

files = parse_names(t, parent_dir, sensor="S30")

tt = open_raster(files, "blue")
print(type(tt))

print(get_band(tt))

import os
import sys
from glob import glob
from xml.etree import ElementTree
from xml.dom import minidom
from typing import Dict, Union, List
from dataclasses import dataclass
import re

import numpy as np
from osgeo import gdal


SENT2_META_HEADERS = [
    "PRODUCT_START_TIME",
    "PRODUCT_STOP_TIME",
    "PRODUCT_URI",
    "PROCESSING_LEVEL",
    "PRODUCT_TYPE",
    "PROCESSING_BASELINE",
    "GENERATION_TIME",
    "SENSING_ORBIT_NUMBER",
    "SENSING_ORBIT_DIRECTION",
    "IMAGE_FILE",
    "SPECIAL_VALUE_TEXT",
    "SPECIAL_VALUE_INDEX",
    "SOLAR_IRRADIANCE",
    "Cloud_Coverage_Assessment",
]

SENT2_BAND_IDS = ["2", "3", "4", "5", "6", "7", "8", "8a", "9", "10", "11", "12"]
R10_BAND_IDS = ["2", "3", "4", "8", "TCI", "AOT", "WVP"]
R20_BAND_IDS = [
    "2",
    "3",
    "4",
    "5",
    "6",
    "7",
    "8a",
    "11",
    "12",
    "TCI",
    "WVP",
    "AOT",
    "SCL",
]
R60_BAND_IDS = [
    "1",
    "2",
    "3",
    "4",
    "5",
    "6",
    "7",
    "8a",
    "9",
    "11",
    "12",
    "TCI",
    "AOT",
    "WVP",
    "SCL",
]
BAND_LISTINGS = [
    "B02",
    "B03",
    "B04",
    "B05",
    "B06",
    "B07",
    "B08",
    "B8A",
    "B09",
    "B10",
    "B11",
    "B12",
    "TCI",
    "AOT",
    "WVP",
    "SCL",
]


@dataclass
class SentMeta:
    dir_path: str
    start_time: str
    stop_time: str
    uri: str
    processing_level: str
    product_type: str
    basetime: str
    generation_time: str
    orbit_number: str
    orbit_direction: str
    image_files: Dict[str, Union[Dict[str, str], str]]
    special_value_text: str
    special_value_index: str
    solar_irradiance: str
    cloud_coverage: str

    def __post_init__(self):
        self.__stringify_attributes()
        image_dict = {}
        if self.processing_level == "Level-2A":
            img_paths = {
                "10": self.__assign_band_ids("R10"),
                "20": self.__assign_band_ids("R20"),
                "60": self.__assign_band_ids("R60"),
            }
            self.image_files = img_paths
        if self.processing_level == "Level-1C":
            img_paths = self.__assign_band_ids()
            self.image_files = img_paths


        """
        for i in range(len(self.image_files) - 1):
            image_dict[SENT2_BAND_IDS[i]] = self.image_files[i]

        self.image_files = image_dict
        """

    def __stringify_attributes(self):
        for att in self.__dict__:
            if len(getattr(self, att)) == 1:
                setattr(self, att, str(getattr(self, att)[0]))

    def __assign_band_ids(self, sub_folder=None, level=1):
        image_dict = {}
        if sub_folder == "R10":
            img_paths = [f"{img}.jp2" for img in self.image_files if sub_folder in img]
        elif sub_folder == "R20":
            img_paths = [f"{img}.jp2" for img in self.image_files if sub_folder in img]
        elif sub_folder == "R60":
            img_paths = [f"{img}.jp2" for img in self.image_files if sub_folder in img]
        else:
            img_paths = [f"{img}.jp2" for img in self.image_files]

        for i in range(len(img_paths)):
            band_id = self.__get_band_id(img_paths[i], level=level)
            image_dict[band_id] = img_paths[i]
        print(image_dict)

        return image_dict

    def __get_band_id(self, path, level=1):
        if level == 1:
            band_id = path[-7: -4]
        else:
            band_id = path[-11:-8]
        if "B" not in band_id:
            return band_id
        elif "B0" in band_id:
            return band_id[-1]
        return band_id[-2:]


@dataclass
class Sentinel(SentMeta):
    sentinel_dir: str

    def get_band(band_number):
        pass


def parse_xml(path):
    xml_meta = glob(os.path.join(path, "MTD*.xml"))[0]
    return ElementTree.parse(xml_meta)


def xml_to_dict(etree_object):
    items = {}
    for elem in tree.iter():
        if "\n" in str(elem.text):
            continue
        if elem.tag not in items:
            items[elem.tag] = [elem.text]
        else:
            items[elem.tag].append(elem.text)
    return items


def pop_sentmeta(parsed_metadata):
    params = {}
    for key in parsed_metadata.keys():
        if key in SENT2_META_HEADERS:
            if key not in params:
                params[key] = parsed_metadata[key]
    return SentMeta(*params.values())


def load_sentinel(sentinel_dir):
    xml_object = parse_xml(sentinel_dir)
    parsed_metadata = xml_to_dict(xml_object)
    params = {"sentinel_dir": sentinel_dir}
    for key in parsed_metadata.keys():
        if key in SENT2_META_HEADERS:
            if key not in params:
                params[key] = parsed_metadata[key]

    return SentMeta(*params.values())


# test = SentMeta("1")
# print(type(test.PRODUCT_START_TIME))
path = "/home/owen/Research/test_data/S2A_MSIL1C_20210720T110621_N0301_R137_T30STE_20210720T132532.SAFE"

tree = parse_xml(path)
meta = xml_to_dict(tree)
sentm = load_sentinel(path)
print(sentm.image_files)

import pytest
import sys

sys.path.append("../rindcalc")

from rindcalc import parse_names


###############################################################################
# DATA


@pytest.fixture
def ls08_names():
    return [
        "LC08_CU_005002_20211209_20211222_C01_V01_LINEAGEQA.tif",
        "LC08_CU_005002_20211209_20211222_C01_V01_PIXELQA.tif",
        "LC08_CU_005002_20211209_20211222_C01_V01_RADSATQA.tif",
        "LC08_CU_005002_20211209_20211222_C01_V01_SEA4.tif",
        "LC08_CU_005002_20211209_20211222_C01_V01_SEZ4.tif",
        "LC08_CU_005002_20211209_20211222_C01_V01_SOA4.tif",
        "LC08_CU_005002_20211209_20211222_C01_V01_SOZ4.tif",
        "LC08_CU_005002_20211209_20211222_C01_V01_TAB1.tif",
        "LC08_CU_005002_20211209_20211222_C01_V01_TAB2.tif",
        "LC08_CU_005002_20211209_20211222_C01_V01_TAB3.tif",
        "LC08_CU_005002_20211209_20211222_C01_V01_TAB4.tif",
        "LC08_CU_005002_20211209_20211222_C01_V01_TAB5.tif",
        "LC08_CU_005002_20211209_20211222_C01_V01_TAB6.tif",
        "LC08_CU_005002_20211209_20211222_C01_V01_TAB7.tif",
        "LC08_CU_005002_20211209_20211222_C01_V01_TAB9.tif",
    ]


@pytest.fixture
def hlsL30_names():
    return [
        "HLS.L30.T11TLM.2021320T184337.v2.0.B01.tif",
        "HLS.L30.T11TLM.2021320T184337.v2.0.B02.tif",
        "HLS.L30.T11TLM.2021320T184337.v2.0.B03.tif",
        "HLS.L30.T11TLM.2021320T184337.v2.0.B04.tif",
        "HLS.L30.T11TLM.2021320T184337.v2.0.B05.tif",
        "HLS.L30.T11TLM.2021320T184337.v2.0.B06.tif",
        "HLS.L30.T11TLM.2021320T184337.v2.0.B07.tif",
        "HLS.L30.T11TLM.2021320T184337.v2.0.B09.tif",
        "HLS.L30.T11TLM.2021320T184337.v2.0.B10.tif",
        "HLS.L30.T11TLM.2021320T184337.v2.0.B11.tif",
        "HLS.L30.T11TLM.2021320T184337.v2.0.Fmask.tif",
        "HLS.L30.T11TLM.2021320T184337.v2.0.SAA.tif",
        "HLS.L30.T11TLM.2021320T184337.v2.0.SZA.tif",
        "HLS.L30.T11TLM.2021320T184337.v2.0.VAA.tif",
        "HLS.L30.T11TLM.2021320T184337.v2.0.VZA.tif",
    ]


@pytest.fixture
def hlsS30_names():
    return [
        "HLS.S30.T11TLM.2021344T185759.v2.0.B01.tif",
        "HLS.S30.T11TLM.2021344T185759.v2.0.B02.tif",
        "HLS.S30.T11TLM.2021344T185759.v2.0.B03.tif",
        "HLS.S30.T11TLM.2021344T185759.v2.0.B04.tif",
        "HLS.S30.T11TLM.2021344T185759.v2.0.B05.tif",
        "HLS.S30.T11TLM.2021344T185759.v2.0.B06.tif",
        "HLS.S30.T11TLM.2021344T185759.v2.0.B07.tif",
        "HLS.S30.T11TLM.2021344T185759.v2.0.B08.tif",
        "HLS.S30.T11TLM.2021344T185759.v2.0.B09.tif",
        "HLS.S30.T11TLM.2021344T185759.v2.0.B8A.tif",
        "HLS.S30.T11TLM.2021344T185759.v2.0.B10.tif",
        "HLS.S30.T11TLM.2021344T185759.v2.0.B11.tif",
        "HLS.S30.T11TLM.2021344T185759.v2.0.B12.tif",
        "HLS.S30.T11TLM.2021344T185759.v2.0.Fmask.tif",
        "HLS.S30.T11TLM.2021344T185759.v2.0.SAA.tif",
        "HLS.S30.T11TLM.2021344T185759.v2.0.SZA.tif",
        "HLS.S30.T11TLM.2021344T185759.v2.0.VAA.tif",
        "HLS.S30.T11TLM.2021344T185759.v2.0.VZA.tif",
    ]


###############################################################################
# TESTS


def test_parse_ls08(ls08_names):
    assert parse_names(ls08_names, parent_dir="./") == {
        "blue": "LC08_CU_005002_20211209_20211222_C01_V01_TAB2.tif",
        "cirrus": "LC08_CU_005002_20211209_20211222_C01_V01_TAB9.tif",
        "coastal aerosol": "LC08_CU_005002_20211209_20211222_C01_V01_TAB1.tif",
        "green": "LC08_CU_005002_20211209_20211222_C01_V01_TAB3.tif",
        "nir broad": None,
        "nir narrow": "LC08_CU_005002_20211209_20211222_C01_V01_TAB5.tif",
        "red": "LC08_CU_005002_20211209_20211222_C01_V01_TAB4.tif",
        "red-edge 1": None,
        "red-edge 2": None,
        "red-edge 3": None,
        "swir 1": "LC08_CU_005002_20211209_20211222_C01_V01_TAB6.tif",
        "swir 2": "LC08_CU_005002_20211209_20211222_C01_V01_TAB7.tif",
        "thermal infrared 1": None,
        "thermal infrared 2": None,
        "water vapor": None,
        "parent": "./",
    }


def test_parse_hlsL30(hlsL30_names):
    assert parse_names(hlsL30_names, parent_dir="./", sensor="L30") == {
        "blue": "HLS.L30.T11TLM.2021320T184337.v2.0.B02.tif",
        "cirrus": "HLS.L30.T11TLM.2021320T184337.v2.0.B09.tif",
        "coastal aerosol": "HLS.L30.T11TLM.2021320T184337.v2.0.B01.tif",
        "green": "HLS.L30.T11TLM.2021320T184337.v2.0.B03.tif",
        "nir broad": None,
        "nir narrow": "HLS.L30.T11TLM.2021320T184337.v2.0.B05.tif",
        "red": "HLS.L30.T11TLM.2021320T184337.v2.0.B04.tif",
        "red-edge 1": None,
        "red-edge 2": None,
        "red-edge 3": None,
        "swir 1": "HLS.L30.T11TLM.2021320T184337.v2.0.B06.tif",
        "swir 2": "HLS.L30.T11TLM.2021320T184337.v2.0.B07.tif",
        "thermal infrared 1": "HLS.L30.T11TLM.2021320T184337.v2.0.B10.tif",
        "thermal infrared 2": "HLS.L30.T11TLM.2021320T184337.v2.0.B11.tif",
        "water vapor": None,
        "parent": "./",
    }


def test_parse_hlsS30(hlsS30_names):
    assert parse_names(hlsS30_names, parent_dir="./", sensor="S30") == {
        "blue": "HLS.S30.T11TLM.2021344T185759.v2.0.B02.tif",
        "cirrus": "HLS.S30.T11TLM.2021344T185759.v2.0.B10.tif",
        "coastal aerosol": "HLS.S30.T11TLM.2021344T185759.v2.0.B01.tif",
        "green": "HLS.S30.T11TLM.2021344T185759.v2.0.B03.tif",
        "nir broad": "HLS.S30.T11TLM.2021344T185759.v2.0.B08.tif",
        "nir narrow": "HLS.S30.T11TLM.2021344T185759.v2.0.B8A.tif",
        "red": "HLS.S30.T11TLM.2021344T185759.v2.0.B04.tif",
        "red-edge 1": "HLS.S30.T11TLM.2021344T185759.v2.0.B05.tif",
        "red-edge 2": "HLS.S30.T11TLM.2021344T185759.v2.0.B06.tif",
        "red-edge 3": "HLS.S30.T11TLM.2021344T185759.v2.0.B07.tif",
        "swir 1": "HLS.S30.T11TLM.2021344T185759.v2.0.B11.tif",
        "swir 2": "HLS.S30.T11TLM.2021344T185759.v2.0.B12.tif",
        "thermal infrared 1": None,
        "thermal infrared 2": None,
        "water vapor": "HLS.S30.T11TLM.2021344T185759.v2.0.B09.tif",
        "parent": "./",
    }

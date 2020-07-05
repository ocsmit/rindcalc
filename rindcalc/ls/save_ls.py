from .cloud_masking import cloud_mask_array
from rindcalc.band_utils import save_raster


def save_ls(out_path, mask_clouds, landsat_dir, equation, bands):
    if out_path is not None and mask_clouds:
        masked = cloud_mask_array(landsat_dir, equation)
        save_raster(masked, out_path, bands["snap"])
        return masked
    if out_path is not None and not mask_clouds:
        save_raster(equation, out_path, bands["snap"])
        return equation
    if out_path is None and mask_clouds:
        masked = cloud_mask_array(landsat_dir, equation)
        return masked
    if out_path is None and not mask_clouds:
        return equation
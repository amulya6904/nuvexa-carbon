import random


def generate_ndvi(crop_type: str, practice_type: str) -> float:
    crop = crop_type.lower()
    practice = practice_type.lower()

    base_ndvi = 0.55

    if crop in ["rice", "wheat", "sugarcane"]:
        base_ndvi += 0.10

    if crop in ["millet", "maize", "pulses"]:
        base_ndvi += 0.05

    if practice in ["organic", "regenerative", "sustainable"]:
        base_ndvi += 0.12

    if practice in ["chemical", "traditional"]:
        base_ndvi -= 0.05

    variation = random.uniform(-0.05, 0.05)

    ndvi = base_ndvi + variation

    return round(max(0.1, min(ndvi, 0.95)), 3)

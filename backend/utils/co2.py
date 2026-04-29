def estimate_co2e(area_hectares: float, crop_type: str, practice_type: str, ndvi_score: float) -> float:
    crop = crop_type.lower()
    practice = practice_type.lower()

    crop_factors = {
        "rice": 2.5,
        "wheat": 2.0,
        "sugarcane": 3.0,
        "maize": 1.8,
        "millet": 1.6,
        "pulses": 1.4
    }

    practice_factors = {
        "organic": 1.3,
        "regenerative": 1.4,
        "sustainable": 1.2,
        "traditional": 1.0,
        "chemical": 0.8
    }

    crop_factor = crop_factors.get(crop, 1.5)
    practice_factor = practice_factors.get(practice, 1.0)

    co2e = area_hectares * crop_factor * practice_factor * ndvi_score

    return round(co2e, 2)

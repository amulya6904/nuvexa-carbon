def check_fraud(ndvi_score: float, co2e: float, area_hectares: float) -> str:
    co2e_per_hectare = co2e / area_hectares

    if ndvi_score < 0.35:
        return "REJECTED"

    if co2e_per_hectare > 8:
        return "FLAGGED"

    if area_hectares > 50:
        return "REVIEW"

    return "CLEAN"

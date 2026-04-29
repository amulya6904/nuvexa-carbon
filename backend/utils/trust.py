def calculate_trust_score(ndvi_score: float, fraud_status: str, practice_type: str):
    score = 0

    score += ndvi_score * 40

    if fraud_status == "CLEAN":
        score += 35
    elif fraud_status == "REVIEW":
        score += 20
    elif fraud_status == "FLAGGED":
        score += 10
    else:
        score += 0

    if practice_type.lower() in ["organic", "regenerative", "sustainable"]:
        score += 20
    else:
        score += 10

    score = round(min(score, 100), 2)

    if score >= 85:
        tier = "Platinum"
    elif score >= 70:
        tier = "Gold"
    elif score >= 55:
        tier = "Silver"
    elif score >= 40:
        tier = "Bronze"
    else:
        tier = "Not Eligible"

    return score, tier

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import SessionLocal
from models import Parcel, CO2Estimate
from schemas import EstimateResponse
from utils.ndvi import generate_ndvi
from utils.co2 import estimate_co2e
from utils.fraud import check_fraud
from utils.trust import calculate_trust_score

router = APIRouter(prefix="/estimate", tags=["Estimate"])


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/{parcel_id}", response_model=EstimateResponse)
def create_estimate(parcel_id: int, db: Session = Depends(get_db)):
    parcel = db.query(Parcel).filter(Parcel.id == parcel_id).first()

    if not parcel:
        raise HTTPException(status_code=404, detail="Parcel not found")

    ndvi_score = generate_ndvi(parcel.crop_type, parcel.practice_type)

    co2e = estimate_co2e(
        parcel.area_hectares,
        parcel.crop_type,
        parcel.practice_type,
        ndvi_score
    )

    fraud_status = check_fraud(ndvi_score, co2e, parcel.area_hectares)

    trust_score, tier = calculate_trust_score(
        ndvi_score,
        fraud_status,
        parcel.practice_type
    )

    estimate = CO2Estimate(
        parcel_id=parcel.id,
        ndvi_score=ndvi_score,
        co2e=co2e,
        fraud_status=fraud_status,
        trust_score=trust_score,
        tier=tier
    )

    db.add(estimate)
    db.commit()
    db.refresh(estimate)

    return estimate

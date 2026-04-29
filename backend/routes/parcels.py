from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import SessionLocal
from models import Parcel, User
from schemas import ParcelCreate, ParcelResponse

router = APIRouter(prefix="/parcels", tags=["Parcels"])


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/add", response_model=ParcelResponse)
def add_parcel(parcel: ParcelCreate, db: Session = Depends(get_db)):
    farmer = db.query(User).filter(User.id == parcel.farmer_id).first()

    if not farmer:
        raise HTTPException(status_code=404, detail="Farmer not found")

    if farmer.role.lower() != "farmer":
        raise HTTPException(status_code=400, detail="Only farmers can add parcels")

    new_parcel = Parcel(
        farmer_id=parcel.farmer_id,
        area_hectares=parcel.area_hectares,
        crop_type=parcel.crop_type,
        state=parcel.state,
        soil_type=parcel.soil_type,
        practice_type=parcel.practice_type
    )

    db.add(new_parcel)
    db.commit()
    db.refresh(new_parcel)

    return new_parcel


@router.get("/all", response_model=list[ParcelResponse])
def get_all_parcels(db: Session = Depends(get_db)):
    return db.query(Parcel).all()


@router.get("/farmer/{farmer_id}", response_model=list[ParcelResponse])
def get_farmer_parcels(farmer_id: int, db: Session = Depends(get_db)):
    return db.query(Parcel).filter(Parcel.farmer_id == farmer_id).all()

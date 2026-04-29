from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import SessionLocal
from models import CO2Estimate, CreditListing, Parcel
from schemas import ListingCreate, ListingResponse

router = APIRouter(prefix="/marketplace", tags=["Marketplace"])


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/create/{estimate_id}", response_model=ListingResponse)
def create_listing(estimate_id: int, listing: ListingCreate, db: Session = Depends(get_db)):
    estimate = db.query(CO2Estimate).filter(CO2Estimate.id == estimate_id).first()

    if not estimate:
        raise HTTPException(status_code=404, detail="Estimate not found")

    if estimate.fraud_status == "REJECTED" or estimate.tier == "Not Eligible":
        raise HTTPException(status_code=400, detail="This estimate is not eligible for listing")

    parcel = db.query(Parcel).filter(Parcel.id == estimate.parcel_id).first()

    new_listing = CreditListing(
        parcel_id=estimate.parcel_id,
        farmer_id=parcel.farmer_id,
        co2e=estimate.co2e,
        trust_score=estimate.trust_score,
        tier=estimate.tier,
        price_per_tonne=listing.price_per_tonne,
        status="ACTIVE"
    )

    db.add(new_listing)
    db.commit()
    db.refresh(new_listing)

    return new_listing


@router.get("/listings", response_model=list[ListingResponse])
def get_listings(db: Session = Depends(get_db)):
    return db.query(CreditListing).all()


@router.get("/listings/{listing_id}", response_model=ListingResponse)
def get_listing(listing_id: int, db: Session = Depends(get_db)):
    listing = db.query(CreditListing).filter(CreditListing.id == listing_id).first()

    if not listing:
        raise HTTPException(status_code=404, detail="Listing not found")

    return listing

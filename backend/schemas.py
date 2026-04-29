from pydantic import BaseModel


class UserCreate(BaseModel):
    email: str
    password: str
    role: str


class UserLogin(BaseModel):
    email: str
    password: str


class UserResponse(BaseModel):
    id: int
    email: str
    role: str

    class Config:
        from_attributes = True


class ParcelCreate(BaseModel):
    farmer_id: int
    area_hectares: float
    crop_type: str
    state: str
    soil_type: str
    practice_type: str


class ParcelResponse(BaseModel):
    id: int
    farmer_id: int
    area_hectares: float
    crop_type: str
    state: str
    soil_type: str
    practice_type: str

    class Config:
        from_attributes = True


class EstimateResponse(BaseModel):
    id: int
    parcel_id: int
    ndvi_score: float
    co2e: float
    fraud_status: str
    trust_score: float
    tier: str

    class Config:
        from_attributes = True


class ListingCreate(BaseModel):
    price_per_tonne: float


class ListingResponse(BaseModel):
    id: int
    parcel_id: int
    farmer_id: int
    co2e: float
    trust_score: float
    tier: str
    price_per_tonne: float
    status: str

    class Config:
        from_attributes = True

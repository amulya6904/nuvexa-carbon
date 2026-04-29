from sqlalchemy import Column, Integer, String, Float, ForeignKey
from database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True)
    password = Column(String)
    role = Column(String)


class Parcel(Base):
    __tablename__ = "parcels"

    id = Column(Integer, primary_key=True, index=True)
    farmer_id = Column(Integer, ForeignKey("users.id"))
    area_hectares = Column(Float)
    crop_type = Column(String)
    state = Column(String)
    soil_type = Column(String)
    practice_type = Column(String)


class CO2Estimate(Base):
    __tablename__ = "co2_estimates"

    id = Column(Integer, primary_key=True, index=True)
    parcel_id = Column(Integer, ForeignKey("parcels.id"))
    ndvi_score = Column(Float)
    co2e = Column(Float)
    fraud_status = Column(String)
    trust_score = Column(Float)
    tier = Column(String)


class CreditListing(Base):
    __tablename__ = "credit_listings"

    id = Column(Integer, primary_key=True, index=True)
    parcel_id = Column(Integer, ForeignKey("parcels.id"))
    farmer_id = Column(Integer, ForeignKey("users.id"))
    co2e = Column(Float)
    trust_score = Column(Float)
    tier = Column(String)
    price_per_tonne = Column(Float)
    status = Column(String)

from fastapi import FastAPI
from database import engine, Base
from routes import auth, parcels, estimate, marketplace

app = FastAPI(title="Nuvexa Carbon Backend")

Base.metadata.create_all(bind=engine)

app.include_router(auth.router)
app.include_router(parcels.router)
app.include_router(estimate.router)
app.include_router(marketplace.router)


@app.get("/")
def home():
    return {"message": "Nuvexa Carbon Backend Running"}

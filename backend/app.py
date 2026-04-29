from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from database import engine, Base
from routes import auth, parcels, estimate, marketplace

app = FastAPI(title="Nuvexa Carbon Backend")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173", "http://127.0.0.1:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

Base.metadata.create_all(bind=engine)

app.include_router(auth.router)
app.include_router(parcels.router)
app.include_router(estimate.router)
app.include_router(marketplace.router)


@app.get("/")
def home():
    return {"message": "Nuvexa Carbon Backend Running"}

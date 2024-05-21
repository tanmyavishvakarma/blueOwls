from fastapi import FastAPI
from app.routers import patients, appointments
from app.database import engine, Base

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(patients.router)
app.include_router(appointments.router)

# app/crud.py
from sqlalchemy.orm import Session
from app import models, schemas

def get_patient(db: Session, patient_id: int):
    return db.query(models.Patient).filter(models.Patient.id == patient_id).first()

def get_patients(db: Session):
    return db.query(models.Patient).all()

def create_patient(db: Session, patient: schemas.PatientCreate):
    db_patient = models.Patient(name=patient.name, mobile_no=patient.mobile_no, email=patient.email)
    db.add(db_patient)
    db.commit()
    db.refresh(db_patient)
    return db_patient

def get_appointments_for_patient(db: Session, patient_id: int):
    return db.query(models.Appointment).filter(models.Appointment.patient_id == patient_id).all()

def create_appointment(db: Session, appointment: schemas.AppointmentCreate):
    db_appointment = models.Appointment(**appointment.dict())
    db.add(db_appointment)
    db.commit()
    db.refresh(db_appointment)
    return db_appointment

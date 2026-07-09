from sqlalchemy import Column, Integer, Text, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from app.db.base import Base


class MedicalRecord(Base):
    __tablename__ = "MedicalRecords"

    MedicalRecordID = Column(Integer, primary_key=True, index=True)

    AppointmentID = Column(Integer, ForeignKey("Appointments.AppointmentID"), unique=True)

    Diagnosis = Column(Text)

    Prescription = Column(Text)

    DoctorNotes = Column(Text)

    CreatedAt = Column(DateTime, server_default=func.now())

    UpdatedAt = Column(DateTime, server_default=func.now(), onupdate=func.now())

    appointment = relationship("Appointment", back_populates="medical_record")
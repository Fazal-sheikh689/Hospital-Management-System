from sqlalchemy import Column, Integer, String, Boolean, Date, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from app.db.base import Base


class Patient(Base):
    __tablename__ = "Patients"

    PatientID = Column(Integer, primary_key=True, index=True)

    FirstName = Column(String(50), nullable=False)

    LastName = Column(String(50), nullable=False)

    Gender = Column(String(10))

    DateOfBirth = Column(Date)

    Phone = Column(String(20))

    Address = Column(String(255))

    CNIC = Column(String(20), unique=True)

    BloodGroup = Column(String(10))

    EmergencyContact = Column(String(20))

    IsActive = Column(Boolean, default=True)

    CreatedAt = Column(DateTime, server_default=func.now())

    UpdatedAt = Column(DateTime, server_default=func.now(), onupdate=func.now())

    appointments = relationship("Appointment", back_populates="patient")
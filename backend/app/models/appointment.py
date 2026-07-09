from sqlalchemy import Column, Integer, Date, Time, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from app.db.base import Base


class Appointment(Base):
    __tablename__ = "Appointments"

    AppointmentID = Column(Integer, primary_key=True, index=True)

    PatientID = Column(Integer, ForeignKey("Patients.PatientID"), nullable=False)

    DoctorID = Column(Integer, ForeignKey("Doctors.DoctorID"), nullable=False)

    AppointmentDate = Column(Date, nullable=False)

    AppointmentTime = Column(Time, nullable=False)

    Status = Column(String(30), nullable=False)

    CreatedAt = Column(DateTime, server_default=func.now())

    UpdatedAt = Column(DateTime, server_default=func.now(), onupdate=func.now())

    patient = relationship("Patient", back_populates="appointments")

    doctor = relationship("Doctor", back_populates="appointments")

    medical_record = relationship(
        "MedicalRecord",
        back_populates="appointment",
        uselist=False
    )

    bill = relationship(
        "Bill",
        back_populates="appointment",
        uselist=False
    )
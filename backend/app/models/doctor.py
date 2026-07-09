from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from app.db.base import Base


class Doctor(Base):
    __tablename__ = "Doctors"

    DoctorID = Column(Integer, primary_key=True, index=True)

    UserID = Column(Integer, ForeignKey("Users.UserID"), unique=True, nullable=False)

    DepartmentID = Column(Integer, ForeignKey("Departments.DepartmentID"), nullable=False)

    FirstName = Column(String(50), nullable=False)

    LastName = Column(String(50), nullable=False)

    Phone = Column(String(20))

    Email = Column(String(100))

    Experience = Column(Integer)

    Qualification = Column(String(100))

    IsActive = Column(Boolean, default=True)

    CreatedAt = Column(DateTime, server_default=func.now())

    UpdatedAt = Column(DateTime, server_default=func.now(), onupdate=func.now())

    user = relationship("User", back_populates="doctor")

    department = relationship("Department", back_populates="doctors")

    appointments = relationship("Appointment", back_populates="doctor")
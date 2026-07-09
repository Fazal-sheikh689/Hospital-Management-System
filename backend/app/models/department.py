from sqlalchemy import Column, Integer, String, Boolean, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from app.db.base import Base


class Department(Base):
    __tablename__ = "Departments"

    DepartmentID = Column(Integer, primary_key=True, index=True)

    DepartmentName = Column(String(100), unique=True, nullable=False)

    Description = Column(String(255))

    IsActive = Column(Boolean, default=True)

    CreatedAt = Column(DateTime, server_default=func.now())

    UpdatedAt = Column(DateTime, server_default=func.now(), onupdate=func.now())

    doctors = relationship("Doctor", back_populates="department")
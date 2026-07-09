from sqlalchemy import Column, Integer, String, DECIMAL, Date, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from app.db.base import Base


class Bill(Base):
    __tablename__ = "Bills"

    BillID = Column(Integer, primary_key=True, index=True)

    AppointmentID = Column(Integer, ForeignKey("Appointments.AppointmentID"), unique=True)

    Amount = Column(DECIMAL(10, 2), nullable=False)

    PaymentStatus = Column(String(30), nullable=False)

    PaymentMethod = Column(String(30))

    BillDate = Column(Date)

    CreatedAt = Column(DateTime, server_default=func.now())

    UpdatedAt = Column(DateTime, server_default=func.now(), onupdate=func.now())

    appointment = relationship("Appointment", back_populates="bill")
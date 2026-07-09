from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from app.db.base import Base


class User(Base):
    __tablename__ = "Users"

    UserID = Column(Integer, primary_key=True, index=True)

    Username = Column(String(50), unique=True, nullable=False)

    PasswordHash = Column(String(255), nullable=False)

    RoleID = Column(Integer, ForeignKey("Roles.RoleID"), nullable=False)

    IsActive = Column(Boolean, default=True)

    CreatedAt = Column(DateTime, server_default=func.now())

    UpdatedAt = Column(DateTime, server_default=func.now(), onupdate=func.now())

    role = relationship("Role", back_populates="users")

    doctor = relationship("Doctor", back_populates="user", uselist=False)
from sqlalchemy import Column, Integer, String
from app.db.base import Base


class Role(Base):
    __tablename__ = "Roles"

    RoleID = Column(Integer, primary_key=True, index=True)
    RoleName = Column(String(50), nullable=False, unique=True)
    Description = Column(String(255))
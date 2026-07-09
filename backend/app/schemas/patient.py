from pydantic import BaseModel
from datetime import date


class PatientBase(BaseModel):
    FirstName: str
    LastName: str
    Gender: str | None = None
    DateOfBirth: date | None = None
    Phone: str | None = None
    Address: str | None = None
    BloodGroup: str | None = None


class PatientCreate(PatientBase):
    pass


class PatientResponse(PatientBase):
    PatientID: int

    model_config = {
        "from_attributes": True
    }
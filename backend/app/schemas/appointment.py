from pydantic import BaseModel
from datetime import date, time


class AppointmentBase(BaseModel):
    PatientID: int
    DoctorID: int
    AppointmentDate: date
    AppointmentTime: time
    Status: str


class AppointmentCreate(AppointmentBase):
    pass


class AppointmentResponse(AppointmentBase):
    AppointmentID: int

    model_config = {
        "from_attributes": True
    }
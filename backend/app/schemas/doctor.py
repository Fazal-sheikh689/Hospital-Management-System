from pydantic import BaseModel


class DoctorBase(BaseModel):
    FirstName: str
    LastName: str
    Phone: str | None = None
    Email: str | None = None
    Qualification: str | None = None
    Experience: int | None = None


class DoctorCreate(DoctorBase):
    UserID: int
    DepartmentID: int


class DoctorResponse(DoctorBase):
    DoctorID: int

    model_config = {
        "from_attributes": True
    }
from pydantic import BaseModel
from decimal import Decimal
from datetime import date


class BillBase(BaseModel):
    AppointmentID: int
    Amount: Decimal
    PaymentStatus: str
    PaymentMethod: str | None = None
    BillDate: date


class BillCreate(BillBase):
    pass


class BillResponse(BillBase):
    BillID: int

    model_config = {
        "from_attributes": True
    }
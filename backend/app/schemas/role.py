from pydantic import BaseModel


class RoleBase(BaseModel):
    RoleName: str
    Description: str | None = None


class RoleCreate(RoleBase):
    pass


class RoleResponse(RoleBase):
    RoleID: int

    model_config = {
        "from_attributes": True
    }
# from fastapi import APIRouter

# router = APIRouter(
#     prefix="/roles",
#     tags=["Roles"]
# )

# @router.get("/")
# def get_roles():
#     return {"message": "Get All Roles"}


from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.db.database import get_db
from app.models.role import Role
from app.repositories.role_repository import RoleRepository
from app.schemas.role import RoleCreate
from app.services.role_service import RoleService

router = APIRouter(
    prefix="/roles",
    tags=["Roles"]
)


@router.get("/")
def get_roles(db: Session = Depends(get_db)):
    return RoleService.get_all_roles(db)


@router.get("/{role_id}")
def get_role(role_id: int, db: Session = Depends(get_db)):
    role = RoleService.get_role_by_id(db, role_id)

    if role is None:
        raise HTTPException(status_code=404, detail="Role not found")

    return role


@router.post("/")
def create_role(role: RoleCreate, db: Session = Depends(get_db)):
    return RoleService.create_role(
        db,
        role.RoleName,
        role.Description
    )


@router.delete("/{role_id}")
def delete_role(role_id: int, db: Session = Depends(get_db)):
    RoleService.delete_role(db, role_id)
    return {"message": "Role deleted successfully"}
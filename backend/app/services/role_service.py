from sqlalchemy.orm import Session

from app.models.role import Role
from app.repositories.role_repository import RoleRepository


class RoleService:

    @staticmethod
    def get_all_roles(db: Session):
        return RoleRepository.get_all(db)

    @staticmethod
    def get_role_by_id(db: Session, role_id: int):
        return RoleRepository.get_by_id(db, role_id)

    @staticmethod
    def create_role(db: Session, role_name: str, description: str = None):

        existing_role = RoleRepository.get_by_name(db, role_name)

        if existing_role:
            raise ValueError("Role already exists.")

        role = Role(
            RoleName=role_name,
            Description=description
        )

        return RoleRepository.create(db, role)

    @staticmethod
    def delete_role(db: Session, role_id: int):

        role = RoleRepository.get_by_id(db, role_id)

        if not role:
            raise ValueError("Role not found.")

        return RoleRepository.delete(db, role)
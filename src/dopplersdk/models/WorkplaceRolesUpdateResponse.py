from .base import BaseModel
from typing import List


class Role(BaseModel):
    def __init__(
        self,
        name: str = None,
        permissions: List[str] = None,
        identifier: str = None,
        created_at: str = None,
        is_custom_role: bool = None,
        is_inline_role: bool = None,
        **kwargs,
    ):
        """
        Initialize Role
        Parameters:
        ----------
            name: str
            permissions: list of RolePermissions
            identifier: str
            created_at: str
            is_custom_role: bool
            is_inline_role: bool
        """
        self.name = name
        self.permissions = permissions
        self.identifier = identifier
        self.created_at = created_at
        self.is_custom_role = is_custom_role
        self.is_inline_role = is_inline_role


class WorkplaceRolesUpdateResponse(BaseModel):
    def __init__(self, role: Role = None, **kwargs):
        """
        Initialize WorkplaceRolesUpdateResponse
        Parameters:
        ----------
            role: Role
        """
        self.role = role

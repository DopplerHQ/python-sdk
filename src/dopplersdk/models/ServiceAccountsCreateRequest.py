from .base import BaseModel
from typing import List


class WorkplaceRole(BaseModel):
    """
    You may provide an identifier OR permissions, but not both
    """

    def __init__(self, identifier: str = None, permissions: List[str] = None, **kwargs):
        """
        Initialize WorkplaceRole
        Parameters:
        ----------
            identifier: str
                Identifier of an existing workplace role
            permissions: list of WorkplaceRolePermissions
                Workplace permissions to grant
        """
        self.identifier = identifier
        self.permissions = permissions


class ServiceAccountsCreateRequest(BaseModel):
    def __init__(
        self, name: str = None, workplace_role: WorkplaceRole = None, **kwargs
    ):
        """
        Initialize ServiceAccountsCreateRequest
        Parameters:
        ----------
            name: str
            workplace_role: WorkplaceRole
                You may provide an identifier OR permissions, but not both
        """
        self.name = name
        self.workplace_role = workplace_role

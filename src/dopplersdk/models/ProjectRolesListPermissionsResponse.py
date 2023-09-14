from .base import BaseModel
from typing import List


class ProjectRolesListPermissionsResponse(BaseModel):
    def __init__(self, permissions: List[str] = None, **kwargs):
        """
        Initialize ProjectRolesListPermissionsResponse
        Parameters:
        ----------
            permissions: list of ProjectRolesListPermissionsResponsePermissions
        """
        self.permissions = permissions

from .base import BaseModel
from typing import List


class ListPermissionsResponse(BaseModel):
    def __init__(self, permissions: List[str] = None, **kwargs):
        """
        Initialize ListPermissionsResponse
        Parameters:
        ----------
            permissions: list of ListPermissionsResponsePermissions
        """
        if permissions is not None:
            self.permissions = permissions

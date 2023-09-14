from .base import BaseModel
from typing import List


class ProjectMembersUpdateRequest(BaseModel):
    def __init__(self, role: str = None, environments: List[str] = None, **kwargs):
        """
        Initialize ProjectMembersUpdateRequest
        Parameters:
        ----------
            role: str
                Identifier of the project role
            environments: list of ProjectMembersUpdateRequestEnvironments
                Environment slugs to grant the member access to
        """
        self.role = role
        self.environments = environments

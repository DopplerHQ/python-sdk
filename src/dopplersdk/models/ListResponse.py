from .base import BaseModel
from typing import List


class DefaultProjectRole(BaseModel):
    def __init__(self, identifier: str = None, **kwargs):
        """
        Initialize DefaultProjectRole
        Parameters:
        ----------
            identifier: str
        """
        if identifier is not None:
            self.identifier = identifier


class ListResponseGroups(BaseModel):
    def __init__(
        self,
        name: str = None,
        slug: str = None,
        created_at: str = None,
        default_project_role: DefaultProjectRole = None,
        **kwargs,
    ):
        """
        Initialize ListResponseGroups
        Parameters:
        ----------
            name: str
            slug: str
            created_at: str
            default_project_role: DefaultProjectRole
        """
        if name is not None:
            self.name = name
        if slug is not None:
            self.slug = slug
        if created_at is not None:
            self.created_at = created_at
        if default_project_role is not None:
            self.default_project_role = default_project_role


class ListResponse(BaseModel):
    def __init__(self, groups: List[ListResponseGroups] = None, **kwargs):
        """
        Initialize ListResponse
        Parameters:
        ----------
            groups: list of ListResponseGroups
        """
        if groups is not None:
            self.groups = groups

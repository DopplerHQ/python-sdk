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
        self.identifier = identifier


class GroupsListResponseGroups(BaseModel):
    def __init__(
        self,
        name: str = None,
        slug: str = None,
        created_at: str = None,
        default_project_role: DefaultProjectRole = None,
        **kwargs,
    ):
        """
        Initialize GroupsListResponseGroups
        Parameters:
        ----------
            name: str
            slug: str
            created_at: str
            default_project_role: DefaultProjectRole
        """
        self.name = name
        self.slug = slug
        self.created_at = created_at
        self.default_project_role = default_project_role


class GroupsListResponse(BaseModel):
    def __init__(self, groups: List[GroupsListResponseGroups] = None, **kwargs):
        """
        Initialize GroupsListResponse
        Parameters:
        ----------
            groups: list of GroupsListResponseGroups
        """
        self.groups = groups

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


class Role(BaseModel):
    def __init__(self, identifier: str = None, **kwargs):
        """
        Initialize Role
        Parameters:
        ----------
            identifier: str
        """
        self.identifier = identifier


class GroupProjects(BaseModel):
    def __init__(self, name: str = None, slug: str = None, role: Role = None, **kwargs):
        """
        Initialize GroupProjects
        Parameters:
        ----------
            name: str
            slug: str
            role: Role
        """
        self.name = name
        self.slug = slug
        self.role = role


class GroupMembers(BaseModel):
    def __init__(self, slug: str = None, type_: str = None, **kwargs):
        """
        Initialize GroupMembers
        Parameters:
        ----------
            slug: str
            type_: str
        """
        self.slug = slug
        self.type_ = type_


class Group(BaseModel):
    def __init__(
        self,
        name: str = None,
        slug: str = None,
        created_at: str = None,
        default_project_role: DefaultProjectRole = None,
        projects: List[GroupProjects] = None,
        members: List[GroupMembers] = None,
        **kwargs,
    ):
        """
        Initialize Group
        Parameters:
        ----------
            name: str
            slug: str
            created_at: str
            default_project_role: DefaultProjectRole
            projects: list of GroupProjects
            members: list of GroupMembers
        """
        self.name = name
        self.slug = slug
        self.created_at = created_at
        self.default_project_role = default_project_role
        self.projects = projects
        self.members = members


class GroupsUpdateResponse(BaseModel):
    def __init__(self, group: Group = None, **kwargs):
        """
        Initialize GroupsUpdateResponse
        Parameters:
        ----------
            group: Group
        """
        self.group = group

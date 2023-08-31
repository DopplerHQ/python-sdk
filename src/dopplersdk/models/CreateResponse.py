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


class Role(BaseModel):
    def __init__(self, identifier: str = None, **kwargs):
        """
        Initialize Role
        Parameters:
        ----------
            identifier: str
        """
        if identifier is not None:
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
        if name is not None:
            self.name = name
        if slug is not None:
            self.slug = slug
        if role is not None:
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
        if slug is not None:
            self.slug = slug
        if type_ is not None:
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
        if name is not None:
            self.name = name
        if slug is not None:
            self.slug = slug
        if created_at is not None:
            self.created_at = created_at
        if default_project_role is not None:
            self.default_project_role = default_project_role
        if projects is not None:
            self.projects = projects
        if members is not None:
            self.members = members


class CreateResponse(BaseModel):
    def __init__(self, group: Group = None, **kwargs):
        """
        Initialize CreateResponse
        Parameters:
        ----------
            group: Group
        """
        if group is not None:
            self.group = group

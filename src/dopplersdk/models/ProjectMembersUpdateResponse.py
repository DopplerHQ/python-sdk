from .base import BaseModel
from typing import List


class Role(BaseModel):
    def __init__(self, identifier: str = None, **kwargs):
        """
        Initialize Role
        Parameters:
        ----------
            identifier: str
        """
        self.identifier = identifier


class Member(BaseModel):
    def __init__(
        self,
        slug: str = None,
        role: Role = None,
        access_all_environments: bool = None,
        environments: List[str] = None,
        type_: str = None,
        **kwargs,
    ):
        """
        Initialize Member
        Parameters:
        ----------
            slug: str
            role: Role
            access_all_environments: bool
            environments: list of MemberEnvironments
            type_: str
        """
        self.slug = slug
        self.role = role
        self.access_all_environments = access_all_environments
        self.environments = environments
        self.type_ = type_


class ProjectMembersUpdateResponse(BaseModel):
    def __init__(self, member: Member = None, **kwargs):
        """
        Initialize ProjectMembersUpdateResponse
        Parameters:
        ----------
            member: Member
        """
        self.member = member

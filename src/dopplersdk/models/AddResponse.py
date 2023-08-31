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
        if identifier is not None:
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
        if slug is not None:
            self.slug = slug
        if role is not None:
            self.role = role
        if access_all_environments is not None:
            self.access_all_environments = access_all_environments
        if environments is not None:
            self.environments = environments
        if type_ is not None:
            self.type_ = type_


class AddResponse(BaseModel):
    def __init__(self, member: Member = None, **kwargs):
        """
        Initialize AddResponse
        Parameters:
        ----------
            member: Member
        """
        if member is not None:
            self.member = member

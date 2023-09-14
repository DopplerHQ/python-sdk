from .base import BaseModel
from typing import List


class WorkplaceRole(BaseModel):
    def __init__(
        self,
        name: str = None,
        permissions: List[str] = None,
        identifier: str = None,
        created_at: str = None,
        is_custom_role: bool = None,
        is_inline_role: bool = None,
        **kwargs,
    ):
        """
        Initialize WorkplaceRole
        Parameters:
        ----------
            name: str
            permissions: list of WorkplaceRolePermissions
            identifier: str
            created_at: str
            is_custom_role: bool
            is_inline_role: bool
        """
        self.name = name
        self.permissions = permissions
        self.identifier = identifier
        self.created_at = created_at
        self.is_custom_role = is_custom_role
        self.is_inline_role = is_inline_role


class InvitesListResponseInvites(BaseModel):
    def __init__(
        self,
        slug: str = None,
        email: str = None,
        created_at: str = None,
        workplace_role: WorkplaceRole = None,
        **kwargs,
    ):
        """
        Initialize InvitesListResponseInvites
        Parameters:
        ----------
            slug: str
            email: str
            created_at: str
            workplace_role: WorkplaceRole
        """
        self.slug = slug
        self.email = email
        self.created_at = created_at
        self.workplace_role = workplace_role


class InvitesListResponse(BaseModel):
    def __init__(self, invites: List[InvitesListResponseInvites] = None, **kwargs):
        """
        Initialize InvitesListResponse
        Parameters:
        ----------
            invites: list of InvitesListResponseInvites
        """
        self.invites = invites

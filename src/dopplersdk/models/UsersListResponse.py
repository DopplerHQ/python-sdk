from .base import BaseModel
from typing import List


class User(BaseModel):
    def __init__(
        self,
        email: str = None,
        name: str = None,
        username: str = None,
        profile_image_url: str = None,
        **kwargs,
    ):
        """
        Initialize User
        Parameters:
        ----------
            email: str
            name: str
            username: str
            profile_image_url: str
        """
        self.email = email
        self.name = name
        self.username = username
        self.profile_image_url = profile_image_url


class UsersListResponseWorkplaceUsers(BaseModel):
    def __init__(
        self,
        id: str = None,
        access: str = None,
        created_at: str = None,
        user: User = None,
        **kwargs,
    ):
        """
        Initialize UsersListResponseWorkplaceUsers
        Parameters:
        ----------
            id: str
            access: str
            created_at: str
            user: User
        """
        self.id = id
        self.access = access
        self.created_at = created_at
        self.user = user


class UsersListResponse(BaseModel):
    def __init__(
        self,
        workplace_users: List[UsersListResponseWorkplaceUsers] = None,
        page: int = None,
        success: bool = None,
        **kwargs,
    ):
        """
        Initialize UsersListResponse
        Parameters:
        ----------
            workplace_users: list of UsersListResponseWorkplaceUsers
            page: int
            success: bool
        """
        self.workplace_users = workplace_users
        self.page = page
        self.success = success

from .base import BaseModel


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


class WorkplaceUser(BaseModel):
    def __init__(
        self,
        id: str = None,
        access: str = None,
        created_at: str = None,
        user: User = None,
        **kwargs,
    ):
        """
        Initialize WorkplaceUser
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


class UsersGetResponse(BaseModel):
    def __init__(
        self, workplace_user: WorkplaceUser = None, success: bool = None, **kwargs
    ):
        """
        Initialize UsersGetResponse
        Parameters:
        ----------
            workplace_user: WorkplaceUser
            success: bool
        """
        self.workplace_user = workplace_user
        self.success = success

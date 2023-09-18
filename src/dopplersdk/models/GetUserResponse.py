from .base import BaseModel


class User(BaseModel):
    def __init__(
        self,
        email: str = None,
        name: str = None,
        username: str = None,
        profile_image_url: str = None,
        mfa_enabled: bool = None,
        thirdparty_sso_enabled: bool = None,
        saml_sso_enabled: bool = None,
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
            mfa_enabled: bool
            thirdparty_sso_enabled: bool
            saml_sso_enabled: bool
        """
        self.email = email
        self.name = name
        self.username = username
        self.profile_image_url = profile_image_url
        self.mfa_enabled = mfa_enabled
        self.thirdparty_sso_enabled = thirdparty_sso_enabled
        self.saml_sso_enabled = saml_sso_enabled


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


class GetUserResponse(BaseModel):
    def __init__(
        self, workplace_user: WorkplaceUser = None, success: bool = None, **kwargs
    ):
        """
        Initialize GetUserResponse
        Parameters:
        ----------
            workplace_user: WorkplaceUser
            success: bool
        """
        self.workplace_user = workplace_user
        self.success = success

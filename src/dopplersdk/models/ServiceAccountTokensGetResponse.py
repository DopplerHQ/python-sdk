from .base import BaseModel


class ApiToken(BaseModel):
    def __init__(
        self,
        name: str = None,
        slug: str = None,
        created_at: str = None,
        last_seen_at: str = None,
        expires_at: str = None,
        **kwargs,
    ):
        """
        Initialize ApiToken
        Parameters:
        ----------
            name: str
            slug: str
            created_at: str
            last_seen_at: str
            expires_at: str
        """
        self.name = name
        self.slug = slug
        self.created_at = created_at
        self.last_seen_at = last_seen_at
        self.expires_at = expires_at


class ServiceAccountTokensGetResponse(BaseModel):
    def __init__(self, api_token: ApiToken = None, success: bool = None, **kwargs):
        """
        Initialize ServiceAccountTokensGetResponse
        Parameters:
        ----------
            api_token: ApiToken
            success: bool
        """
        self.api_token = api_token
        self.success = success

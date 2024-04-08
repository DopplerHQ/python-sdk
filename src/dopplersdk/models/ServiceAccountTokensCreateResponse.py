from .base import BaseModel
from typing import Any


class ApiToken(BaseModel):
    def __init__(
        self,
        name: str = None,
        slug: str = None,
        created_at: str = None,
        last_seen_at: Any = None,
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
            last_seen_at
            expires_at: str
        """
        self.name = name
        self.slug = slug
        self.created_at = created_at
        self.last_seen_at = last_seen_at
        self.expires_at = expires_at


class ServiceAccountTokensCreateResponse(BaseModel):
    def __init__(
        self,
        api_token: ApiToken = None,
        api_key: str = None,
        success: bool = None,
        **kwargs,
    ):
        """
        Initialize ServiceAccountTokensCreateResponse
        Parameters:
        ----------
            api_token: ApiToken
            api_key: str
            success: bool
        """
        self.api_token = api_token
        self.api_key = api_key
        self.success = success

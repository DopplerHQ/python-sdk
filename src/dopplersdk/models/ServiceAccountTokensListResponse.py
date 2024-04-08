from .base import BaseModel
from typing import List


class ServiceAccountTokensListResponseApiTokens(BaseModel):
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
        Initialize ServiceAccountTokensListResponseApiTokens
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


class ServiceAccountTokensListResponse(BaseModel):
    def __init__(
        self,
        api_tokens: List[ServiceAccountTokensListResponseApiTokens] = None,
        success: bool = None,
        **kwargs,
    ):
        """
        Initialize ServiceAccountTokensListResponse
        Parameters:
        ----------
            api_tokens: list of ServiceAccountTokensListResponseApiTokens
            success: bool
        """
        self.api_tokens = api_tokens
        self.success = success

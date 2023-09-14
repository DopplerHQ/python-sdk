from .base import BaseModel
from typing import List
from typing import Any


class ServiceTokensListResponseTokens(BaseModel):
    def __init__(
        self,
        name: str = None,
        slug: str = None,
        created_at: str = None,
        config: str = None,
        environment: str = None,
        project: str = None,
        expires_at: Any = None,
        **kwargs,
    ):
        """
        Initialize ServiceTokensListResponseTokens
        Parameters:
        ----------
            name: str
            slug: str
            created_at: str
            config: str
            environment: str
            project: str
            expires_at
        """
        self.name = name
        self.slug = slug
        self.created_at = created_at
        self.config = config
        self.environment = environment
        self.project = project
        self.expires_at = expires_at


class ServiceTokensListResponse(BaseModel):
    def __init__(self, tokens: List[ServiceTokensListResponseTokens] = None, **kwargs):
        """
        Initialize ServiceTokensListResponse
        Parameters:
        ----------
            tokens: list of ServiceTokensListResponseTokens
        """
        self.tokens = tokens

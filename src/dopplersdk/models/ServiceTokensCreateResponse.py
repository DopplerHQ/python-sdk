from .base import BaseModel
from typing import Any


class ServiceTokensCreateResponse(BaseModel):
    def __init__(
        self,
        name: str = None,
        slug: str = None,
        created_at: str = None,
        key: str = None,
        config: str = None,
        environment: str = None,
        project: str = None,
        expires_at: Any = None,
        access: str = None,
        **kwargs,
    ):
        """
        Initialize ServiceTokensCreateResponse
        Parameters:
        ----------
            name: str
            slug: str
            created_at: str
            key: str
            config: str
            environment: str
            project: str
            expires_at
            access: str
        """
        self.name = name
        self.slug = slug
        self.created_at = created_at
        self.key = key
        self.config = config
        self.environment = environment
        self.project = project
        self.expires_at = expires_at
        self.access = access

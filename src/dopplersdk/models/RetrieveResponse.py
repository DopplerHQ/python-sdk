from .base import BaseModel
from typing import Any


class User(BaseModel):
    def __init__(
        self,
        email: str = None,
        name: str = None,
        profile_image_url: str = None,
        **kwargs,
    ):
        """
        Initialize User
        Parameters:
        ----------
            email: str
            name: str
            profile_image_url: str
        """
        self.email = email
        self.name = name
        self.profile_image_url = profile_image_url


class Log(BaseModel):
    def __init__(
        self,
        id: str = None,
        text: str = None,
        html: str = None,
        created_at: str = None,
        config: Any = None,
        environment: str = None,
        project: str = None,
        user: User = None,
        **kwargs,
    ):
        """
        Initialize Log
        Parameters:
        ----------
            id: str
            text: str
            html: str
            created_at: str
            config
            environment: str
            project: str
            user: User
        """
        self.id = id
        self.text = text
        self.html = html
        self.created_at = created_at
        self.config = config
        self.environment = environment
        self.project = project
        self.user = user


class RetrieveResponse(BaseModel):
    def __init__(self, log: Log = None, **kwargs):
        """
        Initialize RetrieveResponse
        Parameters:
        ----------
            log: Log
        """
        self.log = log

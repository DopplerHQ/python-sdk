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
        if email is not None:
            self.email = email
        if name is not None:
            self.name = name
        if profile_image_url is not None:
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
        if id is not None:
            self.id = id
        if text is not None:
            self.text = text
        if html is not None:
            self.html = html
        if created_at is not None:
            self.created_at = created_at
        if config is not None:
            self.config = config
        if environment is not None:
            self.environment = environment
        if project is not None:
            self.project = project
        if user is not None:
            self.user = user


class ActivityLogsRetrieve200Response(BaseModel):
    def __init__(self, log: Log = None, **kwargs):
        """
        Initialize ActivityLogsRetrieve200Response
        Parameters:
        ----------
            log: Log
        """
        if log is not None:
            self.log = log

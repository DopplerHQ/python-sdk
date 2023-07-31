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
        if email is not None:
            self.email = email
        if name is not None:
            self.name = name
        if username is not None:
            self.username = username
        if profile_image_url is not None:
            self.profile_image_url = profile_image_url


class ConfigLogsList200ResponseLogs(BaseModel):
    def __init__(
        self,
        id: str = None,
        text: str = None,
        html: str = None,
        rollback: bool = None,
        created_at: str = None,
        config: str = None,
        environment: str = None,
        project: str = None,
        user: User = None,
        **kwargs,
    ):
        """
        Initialize ConfigLogsList200ResponseLogs
        Parameters:
        ----------
            id: str
            text: str
            html: str
            rollback: bool
            created_at: str
            config: str
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
        if rollback is not None:
            self.rollback = rollback
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


class ConfigLogsList200Response(BaseModel):
    def __init__(
        self,
        page: int = None,
        logs: List[ConfigLogsList200ResponseLogs] = None,
        **kwargs,
    ):
        """
        Initialize ConfigLogsList200Response
        Parameters:
        ----------
            page: int
            logs: list of ConfigLogsList200ResponseLogs
        """
        if page is not None:
            self.page = page
        if logs is not None:
            self.logs = logs

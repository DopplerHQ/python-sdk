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
        self.email = email
        self.name = name
        self.username = username
        self.profile_image_url = profile_image_url


class ConfigLogsListResponseLogs(BaseModel):
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
        Initialize ConfigLogsListResponseLogs
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
        self.id = id
        self.text = text
        self.html = html
        self.rollback = rollback
        self.created_at = created_at
        self.config = config
        self.environment = environment
        self.project = project
        self.user = user


class ConfigLogsListResponse(BaseModel):
    def __init__(
        self, page: int = None, logs: List[ConfigLogsListResponseLogs] = None, **kwargs
    ):
        """
        Initialize ConfigLogsListResponse
        Parameters:
        ----------
            page: int
            logs: list of ConfigLogsListResponseLogs
        """
        self.page = page
        self.logs = logs

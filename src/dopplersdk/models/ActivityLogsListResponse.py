from .base import BaseModel
from typing import List
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


class ActivityLogsListResponseLogs(BaseModel):
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
        Initialize ActivityLogsListResponseLogs
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


class ActivityLogsListResponse(BaseModel):
    def __init__(
        self,
        page: int = None,
        logs: List[ActivityLogsListResponseLogs] = None,
        **kwargs,
    ):
        """
        Initialize ActivityLogsListResponse
        Parameters:
        ----------
            page: int
            logs: list of ActivityLogsListResponseLogs
        """
        self.page = page
        self.logs = logs

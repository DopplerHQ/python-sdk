from .base import BaseModel
from typing import List


class LogDiff(BaseModel):
    def __init__(self, name: str = None, added: str = None, **kwargs):
        """
        Initialize LogDiff
        Parameters:
        ----------
            name: str
            added: str
        """
        self.name = name
        self.added = added


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


class Log(BaseModel):
    def __init__(
        self,
        id: str = None,
        text: str = None,
        html: str = None,
        diff: List[LogDiff] = None,
        rollback: bool = None,
        created_at: str = None,
        config: str = None,
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
            diff: list of LogDiff
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
        self.diff = diff
        self.rollback = rollback
        self.created_at = created_at
        self.config = config
        self.environment = environment
        self.project = project
        self.user = user


class ConfigLogsGetResponse(BaseModel):
    def __init__(self, log: Log = None, **kwargs):
        """
        Initialize ConfigLogsGetResponse
        Parameters:
        ----------
            log: Log
        """
        self.log = log

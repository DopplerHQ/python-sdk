from .base import BaseModel
from typing import List


class LogDiff(BaseModel):
    def __init__(self, name: str = None, removed: str = None, **kwargs):
        """
        Initialize LogDiff
        Parameters:
        ----------
            name: str
            removed: str
        """
        if name is not None:
            self.name = name
        if removed is not None:
            self.removed = removed


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
        if id is not None:
            self.id = id
        if text is not None:
            self.text = text
        if html is not None:
            self.html = html
        if diff is not None:
            self.diff = diff
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


class ConfigLogsRollback200Response(BaseModel):
    def __init__(self, log: Log = None, **kwargs):
        """
        Initialize ConfigLogsRollback200Response
        Parameters:
        ----------
            log: Log
        """
        if log is not None:
            self.log = log

from .base import BaseModel


class Config(BaseModel):
    def __init__(
        self,
        name: str = None,
        root: bool = None,
        locked: bool = None,
        initial_fetch_at: str = None,
        last_fetch_at: str = None,
        created_at: str = None,
        environment: str = None,
        project: str = None,
        **kwargs,
    ):
        """
        Initialize Config
        Parameters:
        ----------
            name: str
            root: bool
            locked: bool
            initial_fetch_at: str
            last_fetch_at: str
            created_at: str
            environment: str
            project: str
        """
        if name is not None:
            self.name = name
        if root is not None:
            self.root = root
        if locked is not None:
            self.locked = locked
        if initial_fetch_at is not None:
            self.initial_fetch_at = initial_fetch_at
        if last_fetch_at is not None:
            self.last_fetch_at = last_fetch_at
        if created_at is not None:
            self.created_at = created_at
        if environment is not None:
            self.environment = environment
        if project is not None:
            self.project = project


class ConfigsCreate200Response(BaseModel):
    def __init__(self, config: Config = None, **kwargs):
        """
        Initialize ConfigsCreate200Response
        Parameters:
        ----------
            config: Config
        """
        if config is not None:
            self.config = config

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
        self.name = name
        self.root = root
        self.locked = locked
        self.initial_fetch_at = initial_fetch_at
        self.last_fetch_at = last_fetch_at
        self.created_at = created_at
        self.environment = environment
        self.project = project


class ConfigsCreateResponse(BaseModel):
    def __init__(self, config: Config = None, **kwargs):
        """
        Initialize ConfigsCreateResponse
        Parameters:
        ----------
            config: Config
        """
        self.config = config

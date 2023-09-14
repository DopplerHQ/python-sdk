from .base import BaseModel


class Environment(BaseModel):
    def __init__(
        self,
        id: str = None,
        name: str = None,
        initial_fetch_at: str = None,
        created_at: str = None,
        project: str = None,
        **kwargs,
    ):
        """
        Initialize Environment
        Parameters:
        ----------
            id: str
            name: str
            initial_fetch_at: str
            created_at: str
            project: str
        """
        self.id = id
        self.name = name
        self.initial_fetch_at = initial_fetch_at
        self.created_at = created_at
        self.project = project


class RenameResponse(BaseModel):
    def __init__(self, environment: Environment = None, **kwargs):
        """
        Initialize RenameResponse
        Parameters:
        ----------
            environment: Environment
        """
        self.environment = environment

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
        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if initial_fetch_at is not None:
            self.initial_fetch_at = initial_fetch_at
        if created_at is not None:
            self.created_at = created_at
        if project is not None:
            self.project = project


class EnvironmentsCreate200Response(BaseModel):
    def __init__(self, environment: Environment = None, **kwargs):
        """
        Initialize EnvironmentsCreate200Response
        Parameters:
        ----------
            environment: Environment
        """
        if environment is not None:
            self.environment = environment

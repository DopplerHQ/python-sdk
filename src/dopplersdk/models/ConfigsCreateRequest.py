from .base import BaseModel


class ConfigsCreateRequest(BaseModel):
    def __init__(self, name: str, environment: str, project: str, **kwargs):
        """
        Initialize ConfigsCreateRequest
        Parameters:
        ----------
            name: str
                Name of the new branch config.
            environment: str
                Identifier for the environment object.
            project: str
                Unique identifier for the project object.
        """
        self.name = name
        self.environment = environment
        self.project = project

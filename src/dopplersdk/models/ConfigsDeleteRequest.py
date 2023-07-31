from .base import BaseModel


class ConfigsDeleteRequest(BaseModel):
    def __init__(self, config: str, project: str, **kwargs):
        """
        Initialize ConfigsDeleteRequest
        Parameters:
        ----------
            config: str
                Name of the config object.
            project: str
                Unique identifier for the project object.
        """
        self.config = config
        self.project = project

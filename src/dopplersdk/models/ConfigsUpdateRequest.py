from .base import BaseModel


class ConfigsUpdateRequest(BaseModel):
    def __init__(self, name: str, config: str, project: str, **kwargs):
        """
        Initialize ConfigsUpdateRequest
        Parameters:
        ----------
            name: str
                The new name of config.
            config: str
                Name of the config object.
            project: str
                Unique identifier for the project object.
        """
        self.name = name
        self.config = config
        self.project = project

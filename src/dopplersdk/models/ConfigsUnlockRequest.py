from .base import BaseModel


class ConfigsUnlockRequest(BaseModel):
    def __init__(self, config: str, project: str, **kwargs):
        """
        Initialize ConfigsUnlockRequest
        Parameters:
        ----------
            config: str
                Name of the config.
            project: str
                Unique identifier for the project object.
        """
        self.config = config
        self.project = project

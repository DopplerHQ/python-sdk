from .base import BaseModel


class LockRequest(BaseModel):
    def __init__(self, config: str, project: str, **kwargs):
        """
        Initialize LockRequest
        Parameters:
        ----------
            config: str
                Name of the config.
            project: str
                Unique identifier for the project object.
        """
        self.config = config
        self.project = project

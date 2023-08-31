from .base import BaseModel


class CloneRequest(BaseModel):
    def __init__(self, name: str, config: str, project: str, **kwargs):
        """
        Initialize CloneRequest
        Parameters:
        ----------
            name: str
                Name of the new branch config.
            config: str
                Name of the branch config being cloned.
            project: str
                Unique identifier for the project object.
        """
        self.name = name
        self.config = config
        self.project = project

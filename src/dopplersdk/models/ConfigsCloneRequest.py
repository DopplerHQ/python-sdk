from .base import BaseModel


class ConfigsCloneRequest(BaseModel):
    def __init__(self, name: str, config: str, project: str, **kwargs):
        """
        Initialize ConfigsCloneRequest
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

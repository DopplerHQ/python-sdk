from .base import BaseModel


class ProjectsDeleteRequest(BaseModel):
    def __init__(self, project: str, **kwargs):
        """
        Initialize ProjectsDeleteRequest
        Parameters:
        ----------
            project: str
                Unique identifier for the project object.
        """
        self.project = project

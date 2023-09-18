from .base import BaseModel


class ProjectsUpdateRequest(BaseModel):
    def __init__(self, name: str, project: str, description: str = None, **kwargs):
        """
        Initialize ProjectsUpdateRequest
        Parameters:
        ----------
            name: str
                Name of the project.
            project: str
                Unique identifier for the project object.
            description: str
                Description of the project.
        """
        self.name = name
        self.project = project
        self.description = description

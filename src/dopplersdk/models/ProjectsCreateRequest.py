from .base import BaseModel


class ProjectsCreateRequest(BaseModel):
    def __init__(self, name: str, description: str = None, **kwargs):
        """
        Initialize ProjectsCreateRequest
        Parameters:
        ----------
            name: str
                Name of project
            description: str
                Description of project
        """
        self.name = name
        if description is not None:
            self.description = description

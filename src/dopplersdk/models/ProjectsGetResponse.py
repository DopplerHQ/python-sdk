from .base import BaseModel


class Project(BaseModel):
    def __init__(
        self,
        id: str = None,
        name: str = None,
        description: str = None,
        created_at: str = None,
        **kwargs,
    ):
        """
        Initialize Project
        Parameters:
        ----------
            id: str
            name: str
            description: str
            created_at: str
        """
        self.id = id
        self.name = name
        self.description = description
        self.created_at = created_at


class ProjectsGetResponse(BaseModel):
    def __init__(self, project: Project = None, **kwargs):
        """
        Initialize ProjectsGetResponse
        Parameters:
        ----------
            project: Project
        """
        self.project = project

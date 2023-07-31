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
        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
        if created_at is not None:
            self.created_at = created_at


class ProjectsCreate200Response(BaseModel):
    def __init__(self, project: Project = None, **kwargs):
        """
        Initialize ProjectsCreate200Response
        Parameters:
        ----------
            project: Project
        """
        if project is not None:
            self.project = project

from .base import BaseModel
from typing import List


class ListResponseProjects(BaseModel):
    def __init__(
        self,
        id: str = None,
        slug: str = None,
        name: str = None,
        description: str = None,
        created_at: str = None,
        **kwargs,
    ):
        """
        Initialize ListResponseProjects
        Parameters:
        ----------
            id: str
            slug: str
            name: str
            description: str
            created_at: str
        """
        self.id = id
        self.slug = slug
        self.name = name
        self.description = description
        self.created_at = created_at


class ListResponse(BaseModel):
    def __init__(
        self, page: int = None, projects: List[ListResponseProjects] = None, **kwargs
    ):
        """
        Initialize ListResponse
        Parameters:
        ----------
            page: int
            projects: list of ListResponseProjects
        """
        self.page = page
        self.projects = projects

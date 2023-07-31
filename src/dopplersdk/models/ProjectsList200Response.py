from .base import BaseModel
from typing import List


class ProjectsList200ResponseProjects(BaseModel):
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
        Initialize ProjectsList200ResponseProjects
        Parameters:
        ----------
            id: str
            slug: str
            name: str
            description: str
            created_at: str
        """
        if id is not None:
            self.id = id
        if slug is not None:
            self.slug = slug
        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
        if created_at is not None:
            self.created_at = created_at


class ProjectsList200Response(BaseModel):
    def __init__(
        self,
        page: int = None,
        projects: List[ProjectsList200ResponseProjects] = None,
        **kwargs,
    ):
        """
        Initialize ProjectsList200Response
        Parameters:
        ----------
            page: int
            projects: list of ProjectsList200ResponseProjects
        """
        if page is not None:
            self.page = page
        if projects is not None:
            self.projects = projects

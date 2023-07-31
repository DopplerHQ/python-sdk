from .base import BaseModel
from typing import List


class EnvironmentsList200ResponseEnvironments(BaseModel):
    def __init__(
        self,
        id: str = None,
        name: str = None,
        initial_fetch_at: str = None,
        created_at: str = None,
        project: str = None,
        **kwargs,
    ):
        """
        Initialize EnvironmentsList200ResponseEnvironments
        Parameters:
        ----------
            id: str
            name: str
            initial_fetch_at: str
            created_at: str
            project: str
        """
        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if initial_fetch_at is not None:
            self.initial_fetch_at = initial_fetch_at
        if created_at is not None:
            self.created_at = created_at
        if project is not None:
            self.project = project


class EnvironmentsList200Response(BaseModel):
    def __init__(
        self,
        environments: List[EnvironmentsList200ResponseEnvironments] = None,
        page: int = None,
        **kwargs,
    ):
        """
        Initialize EnvironmentsList200Response
        Parameters:
        ----------
            environments: list of EnvironmentsList200ResponseEnvironments
            page: int
        """
        if environments is not None:
            self.environments = environments
        if page is not None:
            self.page = page

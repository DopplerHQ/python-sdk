from .base import BaseModel
from typing import List


class EnvironmentsListResponseEnvironments(BaseModel):
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
        Initialize EnvironmentsListResponseEnvironments
        Parameters:
        ----------
            id: str
            name: str
            initial_fetch_at: str
            created_at: str
            project: str
        """
        self.id = id
        self.name = name
        self.initial_fetch_at = initial_fetch_at
        self.created_at = created_at
        self.project = project


class EnvironmentsListResponse(BaseModel):
    def __init__(
        self,
        environments: List[EnvironmentsListResponseEnvironments] = None,
        page: int = None,
        **kwargs,
    ):
        """
        Initialize EnvironmentsListResponse
        Parameters:
        ----------
            environments: list of EnvironmentsListResponseEnvironments
            page: int
        """
        self.environments = environments
        self.page = page

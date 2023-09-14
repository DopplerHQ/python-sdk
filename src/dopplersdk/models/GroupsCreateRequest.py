from .base import BaseModel


class GroupsCreateRequest(BaseModel):
    def __init__(self, name: str, default_project_role: str = None, **kwargs):
        """
        Initialize GroupsCreateRequest
        Parameters:
        ----------
            name: str
            default_project_role: str
                Identifier of the project role
        """
        self.name = name
        self.default_project_role = default_project_role

from .base import BaseModel


class GroupsUpdateRequest(BaseModel):
    def __init__(self, name: str = None, default_project_role: str = None, **kwargs):
        """
        Initialize GroupsUpdateRequest
        Parameters:
        ----------
            name: str
            default_project_role: str
                Identifier of the project role
        """
        self.name = name
        self.default_project_role = default_project_role

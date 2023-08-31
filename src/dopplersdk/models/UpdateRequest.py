from .base import BaseModel


class UpdateRequest(BaseModel):
    def __init__(self, name: str = None, default_project_role: str = None, **kwargs):
        """
        Initialize UpdateRequest
        Parameters:
        ----------
            name: str
            default_project_role: str
                Identifier of the project role
        """
        if name is not None:
            self.name = name
        if default_project_role is not None:
            self.default_project_role = default_project_role

from .base import BaseModel


class CreateRequest(BaseModel):
    def __init__(self, name: str, default_project_role: str = None, **kwargs):
        """
        Initialize CreateRequest
        Parameters:
        ----------
            name: str
            default_project_role: str
                Identifier of the project role
        """
        self.name = name
        if default_project_role is not None:
            self.default_project_role = default_project_role

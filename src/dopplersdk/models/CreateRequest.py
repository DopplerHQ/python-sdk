from .base import BaseModel


class CreateRequest(BaseModel):
    def __init__(self, name: str, description: str = None, **kwargs):
        """
        Initialize CreateRequest
        Parameters:
        ----------
            name: str
                Name of project
            description: str
                Description of project
        """
        self.name = name
        self.description = description

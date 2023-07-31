from .base import BaseModel


class EnvironmentsCreateRequest(BaseModel):
    def __init__(self, slug: str, name: str, **kwargs):
        """
        Initialize EnvironmentsCreateRequest
        Parameters:
        ----------
            slug: str
            name: str
        """
        self.slug = slug
        self.name = name

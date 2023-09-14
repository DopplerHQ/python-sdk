from .base import BaseModel


class RenameRequest(BaseModel):
    def __init__(self, name: str = None, slug: str = None, **kwargs):
        """
        Initialize RenameRequest
        Parameters:
        ----------
            name: str
                Desired name
            slug: str
                Desired slug
        """
        self.name = name
        self.slug = slug

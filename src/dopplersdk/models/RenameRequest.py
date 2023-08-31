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
        if name is not None:
            self.name = name
        if slug is not None:
            self.slug = slug

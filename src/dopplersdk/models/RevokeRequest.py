from .base import BaseModel


class RevokeRequest(BaseModel):
    def __init__(self, token: str, **kwargs):
        """
        Initialize RevokeRequest
        Parameters:
        ----------
            token: str
        """
        self.token = token

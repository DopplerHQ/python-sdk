from .base import BaseModel


class ServiceAccountTokensCreateRequest(BaseModel):
    def __init__(self, name: str = None, expires_at: str = None, **kwargs):
        """
        Initialize ServiceAccountTokensCreateRequest
        Parameters:
        ----------
            name: str
                The display name of the API token
            expires_at: str
                The datetime at which the API token should expire. If not provided, the API token will remain vaild indefinitely unless manually revoked
        """
        self.name = name
        self.expires_at = expires_at

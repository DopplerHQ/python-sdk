from .base import BaseModel


class ServiceTokensDelete200Response(BaseModel):
    def __init__(self, success: bool = None, **kwargs):
        """
        Initialize ServiceTokensDelete200Response
        Parameters:
        ----------
            success: bool
        """
        if success is not None:
            self.success = success

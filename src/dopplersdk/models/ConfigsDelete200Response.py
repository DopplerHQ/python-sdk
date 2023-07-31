from .base import BaseModel


class ConfigsDelete200Response(BaseModel):
    def __init__(self, success: bool = None, **kwargs):
        """
        Initialize ConfigsDelete200Response
        Parameters:
        ----------
            success: bool
        """
        if success is not None:
            self.success = success

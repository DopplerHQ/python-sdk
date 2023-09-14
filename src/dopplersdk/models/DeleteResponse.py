from .base import BaseModel


class DeleteResponse(BaseModel):
    def __init__(self, success: bool = None, **kwargs):
        """
        Initialize DeleteResponse
        Parameters:
        ----------
            success: bool
        """
        self.success = success

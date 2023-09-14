from .base import BaseModel


class RevokeLeaseResponse(BaseModel):
    def __init__(self, success: bool = None, **kwargs):
        """
        Initialize RevokeLeaseResponse
        Parameters:
        ----------
            success: bool
        """
        self.success = success

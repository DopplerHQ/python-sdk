from .base import BaseModel


class AddTrustedIpResponse(BaseModel):
    def __init__(self, ip: str = None, **kwargs):
        """
        Initialize AddTrustedIpResponse
        Parameters:
        ----------
            ip: str
        """
        self.ip = ip

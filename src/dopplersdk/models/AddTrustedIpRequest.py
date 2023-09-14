from .base import BaseModel


class AddTrustedIpRequest(BaseModel):
    def __init__(self, ip: str, **kwargs):
        """
        Initialize AddTrustedIpRequest
        Parameters:
        ----------
            ip: str
                An IP address or CIDR range
        """
        self.ip = ip

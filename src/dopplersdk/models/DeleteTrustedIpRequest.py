from .base import BaseModel


class DeleteTrustedIpRequest(BaseModel):
    def __init__(self, ip: str, **kwargs):
        """
        Initialize DeleteTrustedIpRequest
        Parameters:
        ----------
            ip: str
                An IP address or CIDR range
        """
        self.ip = ip

from .base import BaseModel


class DeleteRequest(BaseModel):
    def __init__(self, ip: str, **kwargs):
        """
        Initialize DeleteRequest
        Parameters:
        ----------
            ip: str
                An IP address or CIDR range
        """
        self.ip = ip

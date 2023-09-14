from .base import BaseModel
from typing import List


class ListTrustedIpsResponse(BaseModel):
    def __init__(self, ips: List[str] = None, **kwargs):
        """
        Initialize ListTrustedIpsResponse
        Parameters:
        ----------
            ips: list of ListTrustedIpsResponseIps
        """
        self.ips = ips

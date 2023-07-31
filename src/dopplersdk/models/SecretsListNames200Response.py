from .base import BaseModel
from typing import List


class SecretsListNames200Response(BaseModel):
    def __init__(self, names: List[str] = None, **kwargs):
        """
        Initialize SecretsListNames200Response
        Parameters:
        ----------
            names: list of SecretsListNames200ResponseNames
        """
        if names is not None:
            self.names = names

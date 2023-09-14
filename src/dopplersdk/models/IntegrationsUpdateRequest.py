from .base import BaseModel


class IntegrationsUpdateRequest(BaseModel):
    def __init__(self, name: str = None, data: str = None, **kwargs):
        """
        Initialize IntegrationsUpdateRequest
        Parameters:
        ----------
            name: str
                The new name of the integration
            data: str
                The new authentication data for the integration
        """
        self.name = name
        self.data = data

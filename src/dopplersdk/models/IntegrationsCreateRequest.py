from .base import BaseModel

"""
The authentication data for the integration
"""
Data = dict


class IntegrationsCreateRequest(BaseModel):
    def __init__(self, type_: str, name: str, data: Data = None, **kwargs):
        """
        Initialize IntegrationsCreateRequest
        Parameters:
        ----------
            type_: str
                The integration type
            name: str
                The name of the integration
            data: Data
                The authentication data for the integration
        """
        self.type_ = type_
        self.name = name
        self.data = data

from .base import BaseModel


class Data(BaseModel):
    """
    The authentication data for the integration
    """

    def __init__(self, **kwargs):
        pass


class IntegrationsCreateRequest(BaseModel):
    def __init__(self, name: str, type_: str, data: Data = None, **kwargs):
        """
        Initialize IntegrationsCreateRequest
        Parameters:
        ----------
            name: str
                The name of the integration
            type_: str
                The integration type
            data: Data
                The authentication data for the integration
        """
        self.name = name
        self.type_ = type_
        if data is not None:
            self.data = data

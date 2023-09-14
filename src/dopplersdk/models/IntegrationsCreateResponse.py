from .base import BaseModel


class Integration(BaseModel):
    def __init__(self, slug: str = None, name: str = None, type_: str = None, **kwargs):
        """
        Initialize Integration
        Parameters:
        ----------
            slug: str
            name: str
            type_: str
        """
        self.slug = slug
        self.name = name
        self.type_ = type_


class IntegrationsCreateResponse(BaseModel):
    def __init__(self, integration: Integration = None, **kwargs):
        """
        Initialize IntegrationsCreateResponse
        Parameters:
        ----------
            integration: Integration
        """
        self.integration = integration

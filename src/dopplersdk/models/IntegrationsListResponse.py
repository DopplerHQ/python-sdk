from .base import BaseModel
from typing import List


class IntegrationsListResponseIntegrations(BaseModel):
    def __init__(
        self,
        slug: str = None,
        name: str = None,
        kind: str = None,
        enabled: bool = None,
        type_: str = None,
        **kwargs,
    ):
        """
        Initialize IntegrationsListResponseIntegrations
        Parameters:
        ----------
            slug: str
            name: str
            kind: str
            enabled: bool
            type_: str
        """
        self.slug = slug
        self.name = name
        self.kind = kind
        self.enabled = enabled
        self.type_ = type_


class IntegrationsListResponse(BaseModel):
    def __init__(
        self,
        integrations: List[IntegrationsListResponseIntegrations] = None,
        success: bool = None,
        **kwargs,
    ):
        """
        Initialize IntegrationsListResponse
        Parameters:
        ----------
            integrations: list of IntegrationsListResponseIntegrations
            success: bool
        """
        self.integrations = integrations
        self.success = success

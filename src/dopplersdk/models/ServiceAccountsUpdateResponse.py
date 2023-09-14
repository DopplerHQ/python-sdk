from .base import BaseModel


class WorkplaceRole(BaseModel):
    def __init__(
        self,
        name: str = None,
        permissions: list = None,
        identifier: str = None,
        created_at: str = None,
        is_custom_role: bool = None,
        is_inline_role: bool = None,
        **kwargs,
    ):
        """
        Initialize WorkplaceRole
        Parameters:
        ----------
            name: str
            permissions: list of objects
            identifier: str
            created_at: str
            is_custom_role: bool
            is_inline_role: bool
        """
        self.name = name
        self.permissions = permissions
        self.identifier = identifier
        self.created_at = created_at
        self.is_custom_role = is_custom_role
        self.is_inline_role = is_inline_role


class ServiceAccount(BaseModel):
    def __init__(
        self,
        name: str = None,
        slug: str = None,
        created_at: str = None,
        workplace_role: WorkplaceRole = None,
        **kwargs,
    ):
        """
        Initialize ServiceAccount
        Parameters:
        ----------
            name: str
            slug: str
            created_at: str
            workplace_role: WorkplaceRole
        """
        self.name = name
        self.slug = slug
        self.created_at = created_at
        self.workplace_role = workplace_role


class ServiceAccountsUpdateResponse(BaseModel):
    def __init__(self, service_account: ServiceAccount = None, **kwargs):
        """
        Initialize ServiceAccountsUpdateResponse
        Parameters:
        ----------
            service_account: ServiceAccount
        """
        self.service_account = service_account

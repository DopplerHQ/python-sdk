from .base import BaseModel
from typing import List


class WorkplaceRolesCreateRequest(BaseModel):
    def __init__(self, permissions: List[str], name: str, **kwargs):
        """
        Initialize WorkplaceRolesCreateRequest
        Parameters:
        ----------
            permissions: list of WorkplaceRolesCreateRequestPermissions
                An array containing the permissions the role has. Valid permissions are: `all_enclave_projects_admin`, `all_enclave_projects`, `billing_manage`, `billing`, `create_enclave_project`, `custom_roles_manage`, `ekm`, `enclave_secrets_referencing`, `logs_audit`, `logs`, `service_account_api_tokens_manage`, `service_account_api_tokens`, `service_accounts_manage`, `service_accounts`, `settings_manage`, `settings`, `team_manage`, `team`, `verified_domains_manage`, `verified_domains`, `workplace_default_environments_manage`, `workplace_default_environments_read`, `workplace_integrations_list`, `workplace_integrations_manage`, `workplace_integrations_read`
            name: str
                The name of the role
        """
        self.permissions = permissions
        self.name = name

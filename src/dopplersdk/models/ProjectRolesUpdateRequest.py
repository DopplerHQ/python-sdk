from .base import BaseModel
from typing import List


class ProjectRolesUpdateRequest(BaseModel):
    def __init__(self, name: str = None, permissions: List[str] = None, **kwargs):
        """
        Initialize ProjectRolesUpdateRequest
        Parameters:
        ----------
            name: str
                The name of the role
            permissions: list of ProjectRolesUpdateRequestPermissions
                An array containing the permissions the role has. Valid permissions are: `enclave_config_logs`, `enclave_project_config_secrets_read`, `enclave_project_config_dynamic_secrets_read`, `enclave_project_config_dynamic_secrets_leases_write`, `enclave_project_config_rotated_secrets_read`, `enclave_config_syncs_manage`, `enclave_project_secrets_notes_manage`, `enclave_project_config_create`, `enclave_project_config_duplicate`, `enclave_project_config_secrets_write`, `enclave_project_config_service_tokens`, `enclave_project_config_trusted_ips`, `enclave_project_config_logs_rollback`, `enclave_project_config_list_all`, `enclave_project_pull_request_create`, `enclave_project_pull_request_respond`, `enclave_project_pull_request_view`, `enclave_secret_reminders`, `enclave_config_access_logs`, `enclave_project_members`, `enclave_project_rename`, `enclave_project_delete`, `enclave_project_webhooks`, `enclave_project_config_dynamic_secrets_manage`, `enclave_project_config_rotated_secrets_manage`, `enclave_project_config_rename`, `enclave_project_config_lock`, `enclave_project_config_delete`, `enclave_project_environment_list_all`, `enclave_project_environment_all`, `enclave_project_environment_order`, `enclave_project_environment_create`, `enclave_project_environment_delete`, `enclave_project_environment_rename`, `enclave_project_environment_settings_manage`, `enclave_project_secrets_referencing`, `enclave_config_secrets_referencing`
        """
        self.name = name
        self.permissions = permissions

"""
Creates a DopplerSDK class.
Generates the main SDK with all available queries as attributes.

Class:
    DopplerSDK
"""

from .net.environment import Environment

from .services.activity_logs import ActivityLogs
from .services.audit import Audit
from .services.auth import Auth
from .services.config_logs import ConfigLogs
from .services.configs import Configs
from .services.dynamic_secrets import DynamicSecrets
from .services.environments import Environments
from .services.get import Get
from .services.groups import Groups
from .services.integrations import Integrations
from .services.invites import Invites
from .services.project_members import ProjectMembers
from .services.project_roles import ProjectRoles
from .services.projects import Projects
from .services.retrieve import Retrieve
from .services.secrets import Secrets
from .services.service_account_tokens import ServiceAccountTokens
from .services.service_accounts import ServiceAccounts
from .services.service_tokens import ServiceTokens
from .services.syncs import Syncs
from .services.users import Users
from .services.webhooks import Webhooks
from .services.workplace import Workplace
from .services.workplace_roles import WorkplaceRoles


class DopplerSDK:
    """
    A class representing the full DopplerSDK SDK

    Attributes
    ----------
    activity_logs : ActivityLogs
    audit : Audit
    auth : Auth
    config_logs : ConfigLogs
    configs : Configs
    dynamic_secrets : DynamicSecrets
    environments : Environments
    get : Get
    groups : Groups
    integrations : Integrations
    invites : Invites
    project_members : ProjectMembers
    project_roles : ProjectRoles
    projects : Projects
    retrieve : Retrieve
    secrets : Secrets
    service_account_tokens : ServiceAccountTokens
    service_accounts : ServiceAccounts
    service_tokens : ServiceTokens
    syncs : Syncs
    users : Users
    webhooks : Webhooks
    workplace : Workplace
    workplace_roles : WorkplaceRoles

    Methods
    -------
    set_base_url(url: str)
        Sets the end URL
    set_access_token(access_token)
        Set the access token
    """

    def __init__(self, access_token="", environment=Environment.DEFAULT) -> None:
        """
        Initializes the DopplerSDK SDK class.
        Parameters
        ----------
        environment: str
            The environment that the SDK is accessing
        access_token : str
            The access token
        """
        self.activity_logs = ActivityLogs(access_token)
        self.audit = Audit(access_token)
        self.auth = Auth(access_token)
        self.config_logs = ConfigLogs(access_token)
        self.configs = Configs(access_token)
        self.dynamic_secrets = DynamicSecrets(access_token)
        self.environments = Environments(access_token)
        self.get = Get(access_token)
        self.groups = Groups(access_token)
        self.integrations = Integrations(access_token)
        self.invites = Invites(access_token)
        self.project_members = ProjectMembers(access_token)
        self.project_roles = ProjectRoles(access_token)
        self.projects = Projects(access_token)
        self.retrieve = Retrieve(access_token)
        self.secrets = Secrets(access_token)
        self.service_account_tokens = ServiceAccountTokens(access_token)
        self.service_accounts = ServiceAccounts(access_token)
        self.service_tokens = ServiceTokens(access_token)
        self.syncs = Syncs(access_token)
        self.users = Users(access_token)
        self.webhooks = Webhooks(access_token)
        self.workplace = Workplace(access_token)
        self.workplace_roles = WorkplaceRoles(access_token)

        self.set_base_url(environment.value)

    def set_base_url(self, url: str) -> None:
        """
        Sets the end URL

        Parameters
        ----------
            url:
                The end URL
        """
        self.activity_logs.set_base_url(url)
        self.audit.set_base_url(url)
        self.auth.set_base_url(url)
        self.config_logs.set_base_url(url)
        self.configs.set_base_url(url)
        self.dynamic_secrets.set_base_url(url)
        self.environments.set_base_url(url)
        self.get.set_base_url(url)
        self.groups.set_base_url(url)
        self.integrations.set_base_url(url)
        self.invites.set_base_url(url)
        self.project_members.set_base_url(url)
        self.project_roles.set_base_url(url)
        self.projects.set_base_url(url)
        self.retrieve.set_base_url(url)
        self.secrets.set_base_url(url)
        self.service_account_tokens.set_base_url(url)
        self.service_accounts.set_base_url(url)
        self.service_tokens.set_base_url(url)
        self.syncs.set_base_url(url)
        self.users.set_base_url(url)
        self.webhooks.set_base_url(url)
        self.workplace.set_base_url(url)
        self.workplace_roles.set_base_url(url)

    def set_access_token(self, token: str) -> None:
        """
        Sets auth token key

        Parameters
        ----------
        token: string
            Auth token value
        """
        self.activity_logs.set_access_token(token)
        self.audit.set_access_token(token)
        self.auth.set_access_token(token)
        self.config_logs.set_access_token(token)
        self.configs.set_access_token(token)
        self.dynamic_secrets.set_access_token(token)
        self.environments.set_access_token(token)
        self.get.set_access_token(token)
        self.groups.set_access_token(token)
        self.integrations.set_access_token(token)
        self.invites.set_access_token(token)
        self.project_members.set_access_token(token)
        self.project_roles.set_access_token(token)
        self.projects.set_access_token(token)
        self.retrieve.set_access_token(token)
        self.secrets.set_access_token(token)
        self.service_account_tokens.set_access_token(token)
        self.service_accounts.set_access_token(token)
        self.service_tokens.set_access_token(token)
        self.syncs.set_access_token(token)
        self.users.set_access_token(token)
        self.webhooks.set_access_token(token)
        self.workplace.set_access_token(token)
        self.workplace_roles.set_access_token(token)


# c029837e0e474b76bc487506e8799df5e3335891efe4fb02bda7a1441840310c

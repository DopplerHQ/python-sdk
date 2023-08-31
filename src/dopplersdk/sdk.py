"""
Creates a DopplerSDK class.
Generates the main SDK with all available queries as attributes.

Class:
    DopplerSDK
"""
from .net.environment import Environment
from .services.projects import Projects
from .services.environments import Environments
from .services.configs import Configs
from .services.secrets import Secrets
from .services.config_logs import ConfigLogs
from .services.v_3 import V3
from .services.activity_logs import ActivityLogs
from .services.service_tokens import ServiceTokens
from .services.dynamic_secrets import DynamicSecrets
from .services.integrations import Integrations
from .services.syncs import Syncs
from .services.trusted_ips import TrustedIps
from .services.workplace_roles import WorkplaceRoles
from .services.project_roles import ProjectRoles
from .services.project_members import ProjectMembers
from .services.invites import Invites
from .services.service_accounts import ServiceAccounts
from .services.groups import Groups


class DopplerSDK:
    """
    A class representing the full DopplerSDK SDK

    Attributes
    ----------
    projects : Projects
    environments : Environments
    configs : Configs
    secrets : Secrets
    config_logs : ConfigLogs
    v_3 : V3
    activity_logs : ActivityLogs
    service_tokens : ServiceTokens
    dynamic_secrets : DynamicSecrets
    integrations : Integrations
    syncs : Syncs
    trusted_ips : TrustedIps
    workplace_roles : WorkplaceRoles
    project_roles : ProjectRoles
    project_members : ProjectMembers
    invites : Invites
    service_accounts : ServiceAccounts
    groups : Groups

    Methods
    -------
    set_bearer_token(bearer_token)
        Set the bearer token
    """

    def __init__(self, bearer_token="", environment=Environment.DEFAULT) -> None:
        """
        Initializes the DopplerSDK SDK class.
        Parameters
        ----------
        environment: str
            The environment that the SDK is accessing
        bearer_token : str
            The bearer token
        """
        self.projects = Projects(bearer_token)
        self.environments = Environments(bearer_token)
        self.configs = Configs(bearer_token)
        self.secrets = Secrets(bearer_token)
        self.config_logs = ConfigLogs(bearer_token)
        self.v_3 = V3(bearer_token)
        self.activity_logs = ActivityLogs(bearer_token)
        self.service_tokens = ServiceTokens(bearer_token)
        self.dynamic_secrets = DynamicSecrets(bearer_token)
        self.integrations = Integrations(bearer_token)
        self.syncs = Syncs(bearer_token)
        self.trusted_ips = TrustedIps(bearer_token)
        self.workplace_roles = WorkplaceRoles(bearer_token)
        self.project_roles = ProjectRoles(bearer_token)
        self.project_members = ProjectMembers(bearer_token)
        self.invites = Invites(bearer_token)
        self.service_accounts = ServiceAccounts(bearer_token)
        self.groups = Groups(bearer_token)

        self.__set_url(environment.value)

    def __set_url(self, url: str) -> None:
        """
        Sets the end URL

        Parameters
        ----------
            url:
                The end URL
        """
        self.projects.set_url(url)
        self.environments.set_url(url)
        self.configs.set_url(url)
        self.secrets.set_url(url)
        self.config_logs.set_url(url)
        self.v_3.set_url(url)
        self.activity_logs.set_url(url)
        self.service_tokens.set_url(url)
        self.dynamic_secrets.set_url(url)
        self.integrations.set_url(url)
        self.syncs.set_url(url)
        self.trusted_ips.set_url(url)
        self.workplace_roles.set_url(url)
        self.project_roles.set_url(url)
        self.project_members.set_url(url)
        self.invites.set_url(url)
        self.service_accounts.set_url(url)
        self.groups.set_url(url)

    def set_bearer_token(self, token: str) -> None:
        """
        Sets bearer token key

        Parameters
        ----------
        token: string
            Bearer token value
        """
        self.projects.set_bearer_token(token)
        self.environments.set_bearer_token(token)
        self.configs.set_bearer_token(token)
        self.secrets.set_bearer_token(token)
        self.config_logs.set_bearer_token(token)
        self.v_3.set_bearer_token(token)
        self.activity_logs.set_bearer_token(token)
        self.service_tokens.set_bearer_token(token)
        self.dynamic_secrets.set_bearer_token(token)
        self.integrations.set_bearer_token(token)
        self.syncs.set_bearer_token(token)
        self.trusted_ips.set_bearer_token(token)
        self.workplace_roles.set_bearer_token(token)
        self.project_roles.set_bearer_token(token)
        self.project_members.set_bearer_token(token)
        self.invites.set_bearer_token(token)
        self.service_accounts.set_bearer_token(token)
        self.groups.set_bearer_token(token)

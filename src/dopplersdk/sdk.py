"""
Creates a DopplerSDK class.
Generates the main SDK with all available queries as attributes.

Class:
    DopplerSDK
"""
from .net.environment import Environment
from .services.projects import Projects
from .services.secrets import Secrets
from .services.config_logs import ConfigLogs
from .services.environments import Environments
from .services.configs import Configs
from .services.activity_logs import ActivityLogs
from .services.workplace import Workplace
from .services.service_tokens import ServiceTokens
from .services.audit import Audit
from .services.dynamic_secrets import DynamicSecrets
from .services.auth import Auth
from .services.integrations import Integrations
from .services.syncs import Syncs
from .services.workplace_roles import WorkplaceRoles
from .services.project_roles import ProjectRoles
from .services.project_members import ProjectMembers
from .services.invites import Invites
from .services.service_accounts import ServiceAccounts
from .services.groups import Groups
from .services.users import Users


class DopplerSDK:
    """
    A class representing the full DopplerSDK SDK

    Attributes
    ----------
    projects : Projects
    secrets : Secrets
    config_logs : ConfigLogs
    environments : Environments
    configs : Configs
    activity_logs : ActivityLogs
    workplace : Workplace
    service_tokens : ServiceTokens
    audit : Audit
    dynamic_secrets : DynamicSecrets
    auth : Auth
    integrations : Integrations
    syncs : Syncs
    workplace_roles : WorkplaceRoles
    project_roles : ProjectRoles
    project_members : ProjectMembers
    invites : Invites
    service_accounts : ServiceAccounts
    groups : Groups
    users : Users

    Methods
    -------
    set_url(url: str)
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
        self.projects = Projects(access_token)
        self.secrets = Secrets(access_token)
        self.config_logs = ConfigLogs(access_token)
        self.environments = Environments(access_token)
        self.configs = Configs(access_token)
        self.activity_logs = ActivityLogs(access_token)
        self.workplace = Workplace(access_token)
        self.service_tokens = ServiceTokens(access_token)
        self.audit = Audit(access_token)
        self.dynamic_secrets = DynamicSecrets(access_token)
        self.auth = Auth(access_token)
        self.integrations = Integrations(access_token)
        self.syncs = Syncs(access_token)
        self.workplace_roles = WorkplaceRoles(access_token)
        self.project_roles = ProjectRoles(access_token)
        self.project_members = ProjectMembers(access_token)
        self.invites = Invites(access_token)
        self.service_accounts = ServiceAccounts(access_token)
        self.groups = Groups(access_token)
        self.users = Users(access_token)

        self.set_url(environment.value)

    def set_url(self, url: str) -> None:
        """
        Sets the end URL

        Parameters
        ----------
            url:
                The end URL
        """
        self.projects.set_url(url)
        self.secrets.set_url(url)
        self.config_logs.set_url(url)
        self.environments.set_url(url)
        self.configs.set_url(url)
        self.activity_logs.set_url(url)
        self.workplace.set_url(url)
        self.service_tokens.set_url(url)
        self.audit.set_url(url)
        self.dynamic_secrets.set_url(url)
        self.auth.set_url(url)
        self.integrations.set_url(url)
        self.syncs.set_url(url)
        self.workplace_roles.set_url(url)
        self.project_roles.set_url(url)
        self.project_members.set_url(url)
        self.invites.set_url(url)
        self.service_accounts.set_url(url)
        self.groups.set_url(url)
        self.users.set_url(url)

    def set_access_token(self, token: str) -> None:
        """
        Sets auth token key

        Parameters
        ----------
        token: string
            Auth token value
        """
        self.projects.set_access_token(token)
        self.secrets.set_access_token(token)
        self.config_logs.set_access_token(token)
        self.environments.set_access_token(token)
        self.configs.set_access_token(token)
        self.activity_logs.set_access_token(token)
        self.workplace.set_access_token(token)
        self.service_tokens.set_access_token(token)
        self.audit.set_access_token(token)
        self.dynamic_secrets.set_access_token(token)
        self.auth.set_access_token(token)
        self.integrations.set_access_token(token)
        self.syncs.set_access_token(token)
        self.workplace_roles.set_access_token(token)
        self.project_roles.set_access_token(token)
        self.project_members.set_access_token(token)
        self.invites.set_access_token(token)
        self.service_accounts.set_access_token(token)
        self.groups.set_access_token(token)
        self.users.set_access_token(token)

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
from .services.v_3 import V3
from .services.service_tokens import ServiceTokens
from .services.dynamic_secrets import DynamicSecrets
from .services.integrations import Integrations
from .services.syncs import Syncs


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
    v_3 : V3
    service_tokens : ServiceTokens
    dynamic_secrets : DynamicSecrets
    integrations : Integrations
    syncs : Syncs

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
        self.secrets = Secrets(bearer_token)
        self.config_logs = ConfigLogs(bearer_token)
        self.environments = Environments(bearer_token)
        self.configs = Configs(bearer_token)
        self.activity_logs = ActivityLogs(bearer_token)
        self.v_3 = V3(bearer_token)
        self.service_tokens = ServiceTokens(bearer_token)
        self.dynamic_secrets = DynamicSecrets(bearer_token)
        self.integrations = Integrations(bearer_token)
        self.syncs = Syncs(bearer_token)

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
        self.secrets.set_url(url)
        self.config_logs.set_url(url)
        self.environments.set_url(url)
        self.configs.set_url(url)
        self.activity_logs.set_url(url)
        self.v_3.set_url(url)
        self.service_tokens.set_url(url)
        self.dynamic_secrets.set_url(url)
        self.integrations.set_url(url)
        self.syncs.set_url(url)

    def set_bearer_token(self, token: str) -> None:
        """
        Sets bearer token key

        Parameters
        ----------
        token: string
            Bearer token value
        """
        self.projects.set_bearer_token(token)
        self.secrets.set_bearer_token(token)
        self.config_logs.set_bearer_token(token)
        self.environments.set_bearer_token(token)
        self.configs.set_bearer_token(token)
        self.activity_logs.set_bearer_token(token)
        self.v_3.set_bearer_token(token)
        self.service_tokens.set_bearer_token(token)
        self.dynamic_secrets.set_bearer_token(token)
        self.integrations.set_bearer_token(token)
        self.syncs.set_bearer_token(token)

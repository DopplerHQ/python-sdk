from .base import BaseModel
from typing import List
from enum import Enum


class Type_(Enum):
    NONE = "None"
    BEARER = "Bearer"
    BASIC = "Basic"

    def list():
        return list(map(lambda x: x.value, Type_._member_map_.values()))


class Authentication(BaseModel):
    def __init__(
        self,
        token: str = None,
        username: str = None,
        password: str = None,
        type_: Type_ = None,
        **kwargs,
    ):
        """
        Initialize Authentication
        Parameters:
        ----------
            token: str
                Used when type = Bearer
            username: str
                Used when type = Basic
            password: str
                Used when type = Basic
            type_: str
        """
        self.token = token
        self.username = username
        self.password = password
        self.type_ = (
            self._enum_matching(type_, Type_.list(), "type_") if type_ else None
        )


class WebhooksUpdateRequest(BaseModel):
    def __init__(
        self,
        url: str = None,
        secret: str = None,
        authentication: Authentication = None,
        payload: str = None,
        enableConfigs: List[str] = None,
        disableConfigs: List[str] = None,
        **kwargs,
    ):
        """
        Initialize WebhooksUpdateRequest
        Parameters:
        ----------
            url: str
                The webhook URL. Must be https
            secret: str
                See: https://docs.doppler.com/docs/webhooks#verify-webhook-with-request-signing
            authentication: Authentication
            payload: str
                See: https://docs.doppler.com/docs/webhooks#default-payload
            enableConfigs: list of WebhooksUpdateRequestEnableConfigs
                Config slugs that the webhook should be enabled for
            disableConfigs: list of WebhooksUpdateRequestDisableConfigs
                Config slugs that the webhook should be disabled for
        """
        self.url = url
        self.secret = secret
        self.authentication = authentication
        self.payload = payload
        self.enableConfigs = enableConfigs
        self.disableConfigs = disableConfigs

from .base import BaseModel
from typing import List


class Secrets(dict):
    def __init__(self, *args, **kwargs):
        dict.__init__(self, *args, **kwargs)


class SecretsUpdateRequestChangeRequests(BaseModel):
    def __init__(
        self,
        value: str,
        originalName: str,
        name: str,
        originalValue: str = None,
        visibility: str = None,
        originalVisibility: str = None,
        shouldPromote: bool = None,
        shouldDelete: bool = None,
        shouldConverge: bool = None,
        **kwargs,
    ):
        """
        Initialize SecretsUpdateRequestChangeRequests
        Parameters:
        ----------
            value: str
                The value the secret should have. Use `null` (an actual `null`, not the string `null`) to leave the existing secret value unchanged.
            originalName: str
                The original name of the secret. Use `null` (an actual `null`, not the string `null`) or omit this parameter for new secrets. If it differs from `name` then a rename is inferred.
            name: str
                The name of the secret.
            originalValue: str
                The value you expect the secret to have before `name` is applied. If specified, the request will only be processed if the provided value matches what's found in Doppler.
            visibility: str
                Must be set to either `masked`, `unmasked`, or `restricted`.
            originalVisibility: str
                Must be set to either `masked`, `unmasked`, or `restricted`. The visibility you expect the secret to have before `visibility` is applied. If specified, the request will only be processed if the provided visibility matches what's found in Doppler.
            shouldPromote: bool
                Defaults to `false`. Can only be set to `true` if the config being updated is a branch config. If set to `true`, the provided secret will be set in both the branch config as well as the root config in that environment.
            shouldDelete: bool
                Defaults to `false`. If set to `true`, will delete the secret matching the `name` field.
            shouldConverge: bool
                Defaults to `false`. Can only be set to `true` if the config being updated is a branch config and there is a secret with the same name in the root config. In this case, the branch secret will inherit the value and visibility type from the root secret.
        """
        self.value = value
        self.originalName = originalName
        self.name = name
        self.originalValue = originalValue
        self.visibility = visibility
        self.originalVisibility = originalVisibility
        self.shouldPromote = shouldPromote
        self.shouldDelete = shouldDelete
        self.shouldConverge = shouldConverge


class SecretsUpdateRequest(BaseModel):
    def __init__(
        self,
        config: str,
        project: str,
        secrets: Secrets = None,
        change_requests: List[SecretsUpdateRequestChangeRequests] = None,
        **kwargs,
    ):
        """
        Initialize SecretsUpdateRequest
        Parameters:
        ----------
            config: str
                Name of the config object.
            project: str
                Unique identifier for the project object.
            secrets: Secrets
                Either `secrets` or `change_requests` is required (can't use both). Object of secrets you would like to save to the config. Try it with the sample secrets below.
            change_requests: list of SecretsUpdateRequestChangeRequests
                Either `secrets` or `change_requests` is required (can't use both). Object of secrets you would like to save to the config. Try it with the sample secrets below.
        """
        self.config = config
        self.project = project
        self.secrets = secrets
        self.change_requests = change_requests

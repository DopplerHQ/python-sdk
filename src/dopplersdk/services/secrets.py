from urllib.parse import quote
from .base import BaseService
from ..models.SecretsUpdateRequest import (
    SecretsUpdateRequest as SecretsUpdateRequestModel,
)
from ..models.SecretsUpdate200Response import (
    SecretsUpdate200Response as SecretsUpdate200ResponseModel,
)
from ..models.SecretsGet200Response import (
    SecretsGet200Response as SecretsGet200ResponseModel,
)
from ..models.SecretsDownload200Response import (
    SecretsDownload200Response as SecretsDownload200ResponseModel,
)
from ..models.SecretsListNames200Response import (
    SecretsListNames200Response as SecretsListNames200ResponseModel,
)
from ..models.SecretsUpdateNoteRequest import (
    SecretsUpdateNoteRequest as SecretsUpdateNoteRequestModel,
)
from ..models.SecretsUpdateNote200Response import (
    SecretsUpdateNote200Response as SecretsUpdateNote200ResponseModel,
)


class Secrets(BaseService):
    def list(
        self,
        config: str,
        project: str,
        accepts: str = None,
        include_dynamic_secrets: bool = None,
        dynamic_secrets_ttl_sec: int = None,
        secrets: str = None,
        include_managed_secrets: bool = None,
    ):
        """
        List
        Parameters:
        ----------
            project: str
                Unique identifier for the project object.
            config: str
                Name of the config object.
            accepts: str
                Available options are: **application/json**, **text/plain**
            include_dynamic_secrets: bool
                Whether or not to issue leases and include dynamic secret values for the config
            dynamic_secrets_ttl_sec: int
                The number of seconds until dynamic leases expire. Must be used with `include_dynamic_secrets`. Defaults to 1800 (30 minutes).
            secrets: str
                A comma-separated list of secrets to include in the response
            include_managed_secrets: bool
                Whether to include Doppler's auto-generated (managed) secrets
        """

        url_endpoint = "/v3/configs/config/secrets"
        headers = {}
        query_params = []
        self._add_required_headers(headers)
        if not project:
            raise ValueError("Parameter project is required, cannot be empty or blank.")
        if project:
            query_params.append(f"project={project}")
        if not config:
            raise ValueError("Parameter config is required, cannot be empty or blank.")
        if config:
            query_params.append(f"config={config}")
        headers["accepts"] = accepts
        if include_dynamic_secrets:
            query_params.append(f"include_dynamic_secrets={include_dynamic_secrets}")
        if dynamic_secrets_ttl_sec:
            query_params.append(f"dynamic_secrets_ttl_sec={dynamic_secrets_ttl_sec}")
        if secrets:
            query_params.append(f"secrets={secrets}")
        if include_managed_secrets:
            query_params.append(f"include_managed_secrets={include_managed_secrets}")
        final_url = self._url_prefix + url_endpoint + "?" + "&".join(query_params)
        res = self._http.get(final_url, headers, True)
        return res

    def update(
        self, request_input: SecretsUpdateRequestModel = None
    ) -> SecretsUpdate200ResponseModel:
        """
        Update
        """

        url_endpoint = "/v3/configs/config/secrets"
        headers = {"Content-type": "application/json"}
        self._add_required_headers(headers)

        final_url = self._url_prefix + url_endpoint
        res = self._http.post(final_url, headers, request_input, True)
        if res and isinstance(res, dict):
            return SecretsUpdate200ResponseModel(**res)
        return res

    def get(self, name: str, config: str, project: str) -> SecretsGet200ResponseModel:
        """
        Retrieve
        Parameters:
        ----------
            project: str
                Unique identifier for the project object.
            config: str
                Name of the config object.
            name: str
                Name of the secret.
        """

        url_endpoint = "/v3/configs/config/secret"
        headers = {}
        query_params = []
        self._add_required_headers(headers)
        if not project:
            raise ValueError("Parameter project is required, cannot be empty or blank.")
        if project:
            query_params.append(f"project={project}")
        if not config:
            raise ValueError("Parameter config is required, cannot be empty or blank.")
        if config:
            query_params.append(f"config={config}")
        if not name:
            raise ValueError("Parameter name is required, cannot be empty or blank.")
        if name:
            query_params.append(f"name={name}")
        final_url = self._url_prefix + url_endpoint + "?" + "&".join(query_params)
        res = self._http.get(final_url, headers, True)
        if res and isinstance(res, dict):
            return SecretsGet200ResponseModel(**res)
        return res

    def download(
        self,
        config: str,
        project: str,
        format: str = None,
        name_transformer: str = None,
        include_dynamic_secrets: bool = None,
        dynamic_secrets_ttl_sec: int = None,
    ) -> SecretsDownload200ResponseModel:
        """
        Download
        Parameters:
        ----------
            project: str
                Unique identifier for the project object. Not required if using a Service Token.
            config: str
                Name of the config object. Not required if using a Service Token.
            format: str
            name_transformer: str
                Transform secret names to a different case
            include_dynamic_secrets: bool
                Whether or not to issue leases and include dynamic secret values for the config
            dynamic_secrets_ttl_sec: int
                The number of seconds until dynamic leases expire. Must be used with `include_dynamic_secrets`. Defaults to 1800 (30 minutes).
        """

        url_endpoint = "/v3/configs/config/secrets/download"
        headers = {}
        query_params = []
        self._add_required_headers(headers)
        if not project:
            raise ValueError("Parameter project is required, cannot be empty or blank.")
        if project:
            query_params.append(f"project={project}")
        if not config:
            raise ValueError("Parameter config is required, cannot be empty or blank.")
        if config:
            query_params.append(f"config={config}")
        if format:
            query_params.append(f"format={format}")
        if name_transformer:
            query_params.append(f"name_transformer={name_transformer}")
        if include_dynamic_secrets:
            query_params.append(f"include_dynamic_secrets={include_dynamic_secrets}")
        if dynamic_secrets_ttl_sec:
            query_params.append(f"dynamic_secrets_ttl_sec={dynamic_secrets_ttl_sec}")
        final_url = self._url_prefix + url_endpoint + "?" + "&".join(query_params)
        res = self._http.get(final_url, headers, True)
        if res and isinstance(res, dict):
            return SecretsDownload200ResponseModel(**res)
        return res

    def list_names(
        self,
        config: str,
        project: str,
        include_dynamic_secrets: bool = None,
        include_managed_secrets: bool = None,
    ) -> SecretsListNames200ResponseModel:
        """
        List
        Parameters:
        ----------
            project: str
                Unique identifier for the project object.
            config: str
                Name of the config object.
            include_dynamic_secrets: bool
                Whether or not to issue leases and include dynamic secret values for the config
            include_managed_secrets: bool
                Whether to include Doppler's auto-generated (managed) secrets
        """

        url_endpoint = "/v3/configs/config/secrets/names"
        headers = {}
        query_params = []
        self._add_required_headers(headers)
        if not project:
            raise ValueError("Parameter project is required, cannot be empty or blank.")
        if project:
            query_params.append(f"project={project}")
        if not config:
            raise ValueError("Parameter config is required, cannot be empty or blank.")
        if config:
            query_params.append(f"config={config}")
        if include_dynamic_secrets:
            query_params.append(f"include_dynamic_secrets={include_dynamic_secrets}")
        if include_managed_secrets:
            query_params.append(f"include_managed_secrets={include_managed_secrets}")
        final_url = self._url_prefix + url_endpoint + "?" + "&".join(query_params)
        res = self._http.get(final_url, headers, True)
        if res and isinstance(res, dict):
            return SecretsListNames200ResponseModel(**res)
        return res

    def update_note(
        self, request_input: SecretsUpdateNoteRequestModel = None
    ) -> SecretsUpdateNote200ResponseModel:
        """
        Note
        """

        url_endpoint = "/v3/configs/config/secrets/note"
        headers = {"Content-type": "application/json"}
        self._add_required_headers(headers)

        final_url = self._url_prefix + url_endpoint
        res = self._http.post(final_url, headers, request_input, True)
        if res and isinstance(res, dict):
            return SecretsUpdateNote200ResponseModel(**res)
        return res

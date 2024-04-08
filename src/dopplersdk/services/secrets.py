from urllib.parse import quote
from ..net import query_serializer
from .base import BaseService
from ..models.SecretsListResponse import SecretsListResponse as SecretsListResponseModel
from ..models.SecretsUpdateRequest import (
    SecretsUpdateRequest as SecretsUpdateRequestModel,
)
from ..models.SecretsUpdateResponse import (
    SecretsUpdateResponse as SecretsUpdateResponseModel,
)
from ..models.SecretsGetResponse import SecretsGetResponse as SecretsGetResponseModel
from ..models.Format import Format as FormatModel
from ..models.NameTransformer import NameTransformer as NameTransformerModel
from ..models.DownloadResponse import DownloadResponse as DownloadResponseModel
from ..models.UpdateNoteRequest import UpdateNoteRequest as UpdateNoteRequestModel
from ..models.UpdateNoteResponse import UpdateNoteResponse as UpdateNoteResponseModel
from ..models.NamesResponse import NamesResponse as NamesResponseModel


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
    ) -> SecretsListResponseModel:
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
        query_params.append(
            query_serializer.serialize_query("form", False, "project", project)
        )
        if not config:
            raise ValueError("Parameter config is required, cannot be empty or blank.")
        query_params.append(
            query_serializer.serialize_query("form", False, "config", config)
        )
        headers["accepts"] = query_serializer.serialize_header(False, accepts)
        if include_dynamic_secrets:
            query_params.append(
                query_serializer.serialize_query(
                    "form", False, "include_dynamic_secrets", include_dynamic_secrets
                )
            )
        if dynamic_secrets_ttl_sec:
            query_params.append(
                query_serializer.serialize_query(
                    "form", False, "dynamic_secrets_ttl_sec", dynamic_secrets_ttl_sec
                )
            )
        if secrets:
            query_params.append(
                query_serializer.serialize_query("form", False, "secrets", secrets)
            )
        if include_managed_secrets:
            query_params.append(
                query_serializer.serialize_query(
                    "form", False, "include_managed_secrets", include_managed_secrets
                )
            )
        final_url = self._url_prefix + url_endpoint + "?" + "&".join(query_params)
        res = self._http.get(final_url, headers, True)
        if res and isinstance(res, dict):
            return SecretsListResponseModel(**res)
        return res

    def update(
        self, request_input: SecretsUpdateRequestModel = None
    ) -> SecretsUpdateResponseModel:
        """
        Update
        """

        url_endpoint = "/v3/configs/config/secrets"
        headers = {"Content-Type": "application/json"}
        self._add_required_headers(headers)

        final_url = self._url_prefix + url_endpoint
        res = self._http.post(final_url, headers, request_input, True)
        if res and isinstance(res, dict):
            return SecretsUpdateResponseModel(**res)
        return res

    def get(self, name: str, config: str, project: str) -> SecretsGetResponseModel:
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
        query_params.append(
            query_serializer.serialize_query("form", False, "project", project)
        )
        if not config:
            raise ValueError("Parameter config is required, cannot be empty or blank.")
        query_params.append(
            query_serializer.serialize_query("form", False, "config", config)
        )
        if not name:
            raise ValueError("Parameter name is required, cannot be empty or blank.")
        query_params.append(
            query_serializer.serialize_query("form", False, "name", name)
        )
        final_url = self._url_prefix + url_endpoint + "?" + "&".join(query_params)
        res = self._http.get(final_url, headers, True)
        if res and isinstance(res, dict):
            return SecretsGetResponseModel(**res)
        return res

    def delete(self, name: str, config: str, project: str):
        """
        Delete
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
        query_params.append(
            query_serializer.serialize_query("form", False, "project", project)
        )
        if not config:
            raise ValueError("Parameter config is required, cannot be empty or blank.")
        query_params.append(
            query_serializer.serialize_query("form", False, "config", config)
        )
        if not name:
            raise ValueError("Parameter name is required, cannot be empty or blank.")
        query_params.append(
            query_serializer.serialize_query("form", False, "name", name)
        )
        final_url = self._url_prefix + url_endpoint + "?" + "&".join(query_params)
        res = self._http.delete(final_url, headers, True)
        return res

    def download(
        self,
        config: str,
        project: str,
        format: FormatModel = None,
        name_transformer: NameTransformerModel = None,
        include_dynamic_secrets: bool = None,
        dynamic_secrets_ttl_sec: int = None,
        secrets: str = None,
    ) -> DownloadResponseModel:
        """
        Download
        Parameters:
        ----------
            project: str
                Unique identifier for the project object. Not required if using a Service Token.
            config: str
                Name of the config object. Not required if using a Service Token.
            format: Format
            name_transformer: NameTransformer
                Transform secret names to a different case
            include_dynamic_secrets: bool
                Whether or not to issue leases and include dynamic secret values for the config
            dynamic_secrets_ttl_sec: int
                The number of seconds until dynamic leases expire. Must be used with `include_dynamic_secrets`. Defaults to 1800 (30 minutes).
            secrets: str
                Comma-delimited list of secrets to include in the download. Defaults to all secrets if left unspecified.
        """

        url_endpoint = "/v3/configs/config/secrets/download"
        headers = {}
        query_params = []
        self._add_required_headers(headers)
        if not project:
            raise ValueError("Parameter project is required, cannot be empty or blank.")
        query_params.append(
            query_serializer.serialize_query("form", False, "project", project)
        )
        if not config:
            raise ValueError("Parameter config is required, cannot be empty or blank.")
        query_params.append(
            query_serializer.serialize_query("form", False, "config", config)
        )
        if format:
            validated_format = self._enum_matching(format, FormatModel.list(), "format")
            query_params.append(
                query_serializer.serialize_query(
                    "form", False, "format", validated_format
                )
            )
        if name_transformer:
            validated_name_transformer = self._enum_matching(
                name_transformer, NameTransformerModel.list(), "name_transformer"
            )
            query_params.append(
                query_serializer.serialize_query(
                    "form", False, "name_transformer", validated_name_transformer
                )
            )
        if include_dynamic_secrets:
            query_params.append(
                query_serializer.serialize_query(
                    "form", False, "include_dynamic_secrets", include_dynamic_secrets
                )
            )
        if dynamic_secrets_ttl_sec:
            query_params.append(
                query_serializer.serialize_query(
                    "form", False, "dynamic_secrets_ttl_sec", dynamic_secrets_ttl_sec
                )
            )
        if secrets:
            query_params.append(
                query_serializer.serialize_query("form", False, "secrets", secrets)
            )
        final_url = self._url_prefix + url_endpoint + "?" + "&".join(query_params)
        res = self._http.get(final_url, headers, True)
        if res and isinstance(res, dict):
            return DownloadResponseModel(**res)
        return res

    def update_note(
        self, request_input: UpdateNoteRequestModel = None
    ) -> UpdateNoteResponseModel:
        """
        Update Note
        """

        url_endpoint = "/v3/configs/config/secrets/note"
        headers = {"Content-Type": "application/json"}
        self._add_required_headers(headers)

        final_url = self._url_prefix + url_endpoint
        res = self._http.post(final_url, headers, request_input, True)
        if res and isinstance(res, dict):
            return UpdateNoteResponseModel(**res)
        return res

    def names(
        self,
        config: str,
        project: str,
        include_dynamic_secrets: bool = None,
        include_managed_secrets: bool = None,
    ) -> NamesResponseModel:
        """
        List Names
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
        query_params.append(
            query_serializer.serialize_query("form", False, "project", project)
        )
        if not config:
            raise ValueError("Parameter config is required, cannot be empty or blank.")
        query_params.append(
            query_serializer.serialize_query("form", False, "config", config)
        )
        if include_dynamic_secrets:
            query_params.append(
                query_serializer.serialize_query(
                    "form", False, "include_dynamic_secrets", include_dynamic_secrets
                )
            )
        if include_managed_secrets:
            query_params.append(
                query_serializer.serialize_query(
                    "form", False, "include_managed_secrets", include_managed_secrets
                )
            )
        final_url = self._url_prefix + url_endpoint + "?" + "&".join(query_params)
        res = self._http.get(final_url, headers, True)
        if res and isinstance(res, dict):
            return NamesResponseModel(**res)
        return res

from urllib.parse import quote
from ..net import query_serializer
from .base import BaseService
from ..models.ConfigsGetResponse import ConfigsGetResponse as ConfigsGetResponseModel
from ..models.ConfigsUpdateRequest import (
    ConfigsUpdateRequest as ConfigsUpdateRequestModel,
)
from ..models.ConfigsUpdateResponse import (
    ConfigsUpdateResponse as ConfigsUpdateResponseModel,
)
from ..models.ConfigsDeleteRequest import (
    ConfigsDeleteRequest as ConfigsDeleteRequestModel,
)
from ..models.DeleteResponse import DeleteResponse as DeleteResponseModel
from ..models.ConfigsListResponse import ConfigsListResponse as ConfigsListResponseModel
from ..models.ConfigsCreateRequest import (
    ConfigsCreateRequest as ConfigsCreateRequestModel,
)
from ..models.ConfigsCreateResponse import (
    ConfigsCreateResponse as ConfigsCreateResponseModel,
)
from ..models.UnlockRequest import UnlockRequest as UnlockRequestModel
from ..models.UnlockResponse import UnlockResponse as UnlockResponseModel
from ..models.CloneRequest import CloneRequest as CloneRequestModel
from ..models.CloneResponse import CloneResponse as CloneResponseModel
from ..models.LockRequest import LockRequest as LockRequestModel
from ..models.LockResponse import LockResponse as LockResponseModel
from ..models.ListTrustedIpsResponse import (
    ListTrustedIpsResponse as ListTrustedIpsResponseModel,
)
from ..models.AddTrustedIpRequest import AddTrustedIpRequest as AddTrustedIpRequestModel
from ..models.AddTrustedIpResponse import (
    AddTrustedIpResponse as AddTrustedIpResponseModel,
)
from ..models.DeleteTrustedIpRequest import (
    DeleteTrustedIpRequest as DeleteTrustedIpRequestModel,
)


class Configs(BaseService):
    def get(self, config: str, project: str) -> ConfigsGetResponseModel:
        """
        Retrieve
        Parameters:
        ----------
            project: str
                Unique identifier for the project object.
            config: str
                Name of the config object.
        """

        url_endpoint = "/v3/configs/config"
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
        final_url = self._url_prefix + url_endpoint + "?" + "&".join(query_params)
        res = self._http.get(final_url, headers, True)
        if res and isinstance(res, dict):
            return ConfigsGetResponseModel(**res)
        return res

    def update(
        self, request_input: ConfigsUpdateRequestModel = None
    ) -> ConfigsUpdateResponseModel:
        """
        Update
        """

        url_endpoint = "/v3/configs/config"
        headers = {"Content-Type": "application/json"}
        self._add_required_headers(headers)

        final_url = self._url_prefix + url_endpoint
        res = self._http.post(final_url, headers, request_input, True)
        if res and isinstance(res, dict):
            return ConfigsUpdateResponseModel(**res)
        return res

    def delete(
        self, request_input: ConfigsDeleteRequestModel = None
    ) -> DeleteResponseModel:
        """
        Delete
        """

        url_endpoint = "/v3/configs/config"
        headers = {"Content-Type": "application/json"}
        self._add_required_headers(headers)

        final_url = self._url_prefix + url_endpoint
        res = self._http.delete(final_url, headers, True)
        if res and isinstance(res, dict):
            return DeleteResponseModel(**res)
        return res

    def list(
        self,
        project: str,
        environment: str = None,
        page: int = None,
        per_page: int = None,
    ) -> ConfigsListResponseModel:
        """
        List
        Parameters:
        ----------
            project: str
                The project's name
            environment: str
                (optional) the environment from which to list configs
            page: int
                Page number
            per_page: int
                Items per page
        """

        url_endpoint = "/v3/configs"
        headers = {}
        query_params = []
        self._add_required_headers(headers)
        if not project:
            raise ValueError("Parameter project is required, cannot be empty or blank.")
        query_params.append(
            query_serializer.serialize_query("form", False, "project", project)
        )
        if environment:
            query_params.append(
                query_serializer.serialize_query(
                    "form", False, "environment", environment
                )
            )
        if page:
            query_params.append(
                query_serializer.serialize_query("form", False, "page", page)
            )
        if per_page:
            query_params.append(
                query_serializer.serialize_query("form", False, "per_page", per_page)
            )
        final_url = self._url_prefix + url_endpoint + "?" + "&".join(query_params)
        res = self._http.get(final_url, headers, True)
        if res and isinstance(res, dict):
            return ConfigsListResponseModel(**res)
        return res

    def create(
        self, request_input: ConfigsCreateRequestModel = None
    ) -> ConfigsCreateResponseModel:
        """
        Create
        """

        url_endpoint = "/v3/configs"
        headers = {"Content-Type": "application/json"}
        self._add_required_headers(headers)

        final_url = self._url_prefix + url_endpoint
        res = self._http.post(final_url, headers, request_input, True)
        if res and isinstance(res, dict):
            return ConfigsCreateResponseModel(**res)
        return res

    def unlock(self, request_input: UnlockRequestModel = None) -> UnlockResponseModel:
        """
        Unlock
        """

        url_endpoint = "/v3/configs/config/unlock"
        headers = {"Content-Type": "application/json"}
        self._add_required_headers(headers)

        final_url = self._url_prefix + url_endpoint
        res = self._http.post(final_url, headers, request_input, True)
        if res and isinstance(res, dict):
            return UnlockResponseModel(**res)
        return res

    def clone(self, request_input: CloneRequestModel = None) -> CloneResponseModel:
        """
        Clone
        """

        url_endpoint = "/v3/configs/config/clone"
        headers = {"Content-Type": "application/json"}
        self._add_required_headers(headers)

        final_url = self._url_prefix + url_endpoint
        res = self._http.post(final_url, headers, request_input, True)
        if res and isinstance(res, dict):
            return CloneResponseModel(**res)
        return res

    def lock(self, request_input: LockRequestModel = None) -> LockResponseModel:
        """
        Lock
        """

        url_endpoint = "/v3/configs/config/lock"
        headers = {"Content-Type": "application/json"}
        self._add_required_headers(headers)

        final_url = self._url_prefix + url_endpoint
        res = self._http.post(final_url, headers, request_input, True)
        if res and isinstance(res, dict):
            return LockResponseModel(**res)
        return res

    def list_trusted_ips(
        self, config: str, project: str
    ) -> ListTrustedIpsResponseModel:
        """
        List
        Parameters:
        ----------
            project: str
            config: str
        """

        url_endpoint = "/v3/configs/config/trusted_ips"
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
        final_url = self._url_prefix + url_endpoint + "?" + "&".join(query_params)
        res = self._http.get(final_url, headers, True)
        if res and isinstance(res, dict):
            return ListTrustedIpsResponseModel(**res)
        return res

    def add_trusted_ip(
        self, config: str, project: str, request_input: AddTrustedIpRequestModel = None
    ) -> AddTrustedIpResponseModel:
        """
        Add
        Parameters:
        ----------
            project: str
            config: str
        """

        url_endpoint = "/v3/configs/config/trusted_ips"
        headers = {"Content-Type": "application/json"}
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
        final_url = self._url_prefix + url_endpoint + "?" + "&".join(query_params)
        res = self._http.post(final_url, headers, request_input, True)
        if res and isinstance(res, dict):
            return AddTrustedIpResponseModel(**res)
        return res

    def delete_trusted_ip(
        self,
        config: str,
        project: str,
        request_input: DeleteTrustedIpRequestModel = None,
    ):
        """
        Delete
        Parameters:
        ----------
            project: str
            config: str
        """

        url_endpoint = "/v3/configs/config/trusted_ips"
        headers = {"Content-Type": "application/json"}
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
        final_url = self._url_prefix + url_endpoint + "?" + "&".join(query_params)
        res = self._http.delete(final_url, headers, True)
        return res

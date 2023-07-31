from urllib.parse import quote
from .base import BaseService
from ..models.ConfigsList200Response import (
    ConfigsList200Response as ConfigsList200ResponseModel,
)
from ..models.ConfigsCreateRequest import (
    ConfigsCreateRequest as ConfigsCreateRequestModel,
)
from ..models.ConfigsCreate200Response import (
    ConfigsCreate200Response as ConfigsCreate200ResponseModel,
)
from ..models.ConfigsGet200Response import (
    ConfigsGet200Response as ConfigsGet200ResponseModel,
)
from ..models.ConfigsUpdateRequest import (
    ConfigsUpdateRequest as ConfigsUpdateRequestModel,
)
from ..models.ConfigsUpdate200Response import (
    ConfigsUpdate200Response as ConfigsUpdate200ResponseModel,
)
from ..models.ConfigsDeleteRequest import (
    ConfigsDeleteRequest as ConfigsDeleteRequestModel,
)
from ..models.ConfigsDelete200Response import (
    ConfigsDelete200Response as ConfigsDelete200ResponseModel,
)
from ..models.ConfigsCloneRequest import ConfigsCloneRequest as ConfigsCloneRequestModel
from ..models.ConfigsClone200Response import (
    ConfigsClone200Response as ConfigsClone200ResponseModel,
)
from ..models.ConfigsLockRequest import ConfigsLockRequest as ConfigsLockRequestModel
from ..models.ConfigsLock200Response import (
    ConfigsLock200Response as ConfigsLock200ResponseModel,
)
from ..models.ConfigsUnlockRequest import (
    ConfigsUnlockRequest as ConfigsUnlockRequestModel,
)
from ..models.ConfigsUnlock200Response import (
    ConfigsUnlock200Response as ConfigsUnlock200ResponseModel,
)


class Configs(BaseService):
    def list(
        self,
        project: str,
        environment: str = None,
        page: int = None,
        per_page: int = None,
    ) -> ConfigsList200ResponseModel:
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
        if project:
            query_params.append(f"project={project}")
        if environment:
            query_params.append(f"environment={environment}")
        if page:
            query_params.append(f"page={page}")
        if per_page:
            query_params.append(f"per_page={per_page}")
        final_url = self._url_prefix + url_endpoint + "?" + "&".join(query_params)
        res = self._http.get(final_url, headers, True)
        if res and isinstance(res, dict):
            return ConfigsList200ResponseModel(**res)
        return res

    def create(
        self, request_input: ConfigsCreateRequestModel = None
    ) -> ConfigsCreate200ResponseModel:
        """
        Create
        """

        url_endpoint = "/v3/configs"
        headers = {"Content-type": "application/json"}
        self._add_required_headers(headers)

        final_url = self._url_prefix + url_endpoint
        res = self._http.post(final_url, headers, request_input, True)
        if res and isinstance(res, dict):
            return ConfigsCreate200ResponseModel(**res)
        return res

    def get(self, config: str, project: str) -> ConfigsGet200ResponseModel:
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
        if project:
            query_params.append(f"project={project}")
        if not config:
            raise ValueError("Parameter config is required, cannot be empty or blank.")
        if config:
            query_params.append(f"config={config}")
        final_url = self._url_prefix + url_endpoint + "?" + "&".join(query_params)
        res = self._http.get(final_url, headers, True)
        if res and isinstance(res, dict):
            return ConfigsGet200ResponseModel(**res)
        return res

    def update(
        self, request_input: ConfigsUpdateRequestModel = None
    ) -> ConfigsUpdate200ResponseModel:
        """
        Update
        """

        url_endpoint = "/v3/configs/config"
        headers = {"Content-type": "application/json"}
        self._add_required_headers(headers)

        final_url = self._url_prefix + url_endpoint
        res = self._http.post(final_url, headers, request_input, True)
        if res and isinstance(res, dict):
            return ConfigsUpdate200ResponseModel(**res)
        return res

    def delete(
        self, request_input: ConfigsDeleteRequestModel = None
    ) -> ConfigsDelete200ResponseModel:
        """
        Delete
        """

        url_endpoint = "/v3/configs/config"
        headers = {"Content-type": "application/json"}
        self._add_required_headers(headers)

        final_url = self._url_prefix + url_endpoint
        res = self._http.delete(final_url, headers, True)
        if res and isinstance(res, dict):
            return ConfigsDelete200ResponseModel(**res)
        return res

    def clone(
        self, request_input: ConfigsCloneRequestModel = None
    ) -> ConfigsClone200ResponseModel:
        """
        Clone
        """

        url_endpoint = "/v3/configs/config/clone"
        headers = {"Content-type": "application/json"}
        self._add_required_headers(headers)

        final_url = self._url_prefix + url_endpoint
        res = self._http.post(final_url, headers, request_input, True)
        if res and isinstance(res, dict):
            return ConfigsClone200ResponseModel(**res)
        return res

    def lock(
        self, request_input: ConfigsLockRequestModel = None
    ) -> ConfigsLock200ResponseModel:
        """
        Lock
        """

        url_endpoint = "/v3/configs/config/lock"
        headers = {"Content-type": "application/json"}
        self._add_required_headers(headers)

        final_url = self._url_prefix + url_endpoint
        res = self._http.post(final_url, headers, request_input, True)
        if res and isinstance(res, dict):
            return ConfigsLock200ResponseModel(**res)
        return res

    def unlock(
        self, request_input: ConfigsUnlockRequestModel = None
    ) -> ConfigsUnlock200ResponseModel:
        """
        Unlock
        """

        url_endpoint = "/v3/configs/config/unlock"
        headers = {"Content-type": "application/json"}
        self._add_required_headers(headers)

        final_url = self._url_prefix + url_endpoint
        res = self._http.post(final_url, headers, request_input, True)
        if res and isinstance(res, dict):
            return ConfigsUnlock200ResponseModel(**res)
        return res

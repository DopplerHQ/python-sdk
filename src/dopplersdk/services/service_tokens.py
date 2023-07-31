from urllib.parse import quote
from .base import BaseService
from ..models.ServiceTokensCreateRequest import (
    ServiceTokensCreateRequest as ServiceTokensCreateRequestModel,
)
from ..models.ServiceTokensDeleteRequest import (
    ServiceTokensDeleteRequest as ServiceTokensDeleteRequestModel,
)
from ..models.ServiceTokensDelete200Response import (
    ServiceTokensDelete200Response as ServiceTokensDelete200ResponseModel,
)


class ServiceTokens(BaseService):
    def list(self, config: str, project: str):
        """
        List
        Parameters:
        ----------
            project: str
                Unique identifier for the project object.
            config: str
                Name of the config object.
        """

        url_endpoint = "/v3/configs/config/tokens"
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
        return res

    def create(self, request_input: ServiceTokensCreateRequestModel = None):
        """
        Create
        """

        url_endpoint = "/v3/configs/config/tokens"
        headers = {"Content-type": "application/json"}
        self._add_required_headers(headers)

        final_url = self._url_prefix + url_endpoint
        res = self._http.post(final_url, headers, request_input, True)
        return res

    def delete(
        self, request_input: ServiceTokensDeleteRequestModel = None
    ) -> ServiceTokensDelete200ResponseModel:
        """
        Delete
        """

        url_endpoint = "/v3/configs/config/tokens/token"
        headers = {"Content-type": "application/json"}
        self._add_required_headers(headers)

        final_url = self._url_prefix + url_endpoint
        res = self._http.delete(final_url, headers, True)
        if res and isinstance(res, dict):
            return ServiceTokensDelete200ResponseModel(**res)
        return res

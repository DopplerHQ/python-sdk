from urllib.parse import quote
from ..net import query_serializer
from .base import BaseService
from ..models.ServiceTokensListResponse import (
    ServiceTokensListResponse as ServiceTokensListResponseModel,
)
from ..models.ServiceTokensCreateRequest import (
    ServiceTokensCreateRequest as ServiceTokensCreateRequestModel,
)
from ..models.ServiceTokensCreateResponse import (
    ServiceTokensCreateResponse as ServiceTokensCreateResponseModel,
)
from ..models.ServiceTokensDeleteRequest import (
    ServiceTokensDeleteRequest as ServiceTokensDeleteRequestModel,
)
from ..models.DeleteResponse import DeleteResponse as DeleteResponseModel


class ServiceTokens(BaseService):
    def list(self, config: str, project: str) -> ServiceTokensListResponseModel:
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
            return ServiceTokensListResponseModel(**res)
        return res

    def create(
        self, request_input: ServiceTokensCreateRequestModel = None
    ) -> ServiceTokensCreateResponseModel:
        """
        Create
        """

        url_endpoint = "/v3/configs/config/tokens"
        headers = {"Content-type": "application/json"}
        self._add_required_headers(headers)

        final_url = self._url_prefix + url_endpoint
        res = self._http.post(final_url, headers, request_input, True)
        if res and isinstance(res, dict):
            return ServiceTokensCreateResponseModel(**res)
        return res

    def delete(
        self, request_input: ServiceTokensDeleteRequestModel = None
    ) -> DeleteResponseModel:
        """
        Delete
        """

        url_endpoint = "/v3/configs/config/tokens/token"
        headers = {"Content-type": "application/json"}
        self._add_required_headers(headers)

        final_url = self._url_prefix + url_endpoint
        res = self._http.delete(final_url, headers, True)
        if res and isinstance(res, dict):
            return DeleteResponseModel(**res)
        return res

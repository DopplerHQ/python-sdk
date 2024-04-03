from urllib.parse import quote
from ..net import query_serializer
from .base import BaseService
from ..models.IntegrationsGetResponse import (
    IntegrationsGetResponse as IntegrationsGetResponseModel,
)
from ..models.IntegrationsUpdateRequest import (
    IntegrationsUpdateRequest as IntegrationsUpdateRequestModel,
)
from ..models.IntegrationsUpdateResponse import (
    IntegrationsUpdateResponse as IntegrationsUpdateResponseModel,
)
from ..models.IntegrationsDeleteResponse import (
    IntegrationsDeleteResponse as IntegrationsDeleteResponseModel,
)
from ..models.IntegrationsListResponse import (
    IntegrationsListResponse as IntegrationsListResponseModel,
)
from ..models.IntegrationsCreateRequest import (
    IntegrationsCreateRequest as IntegrationsCreateRequestModel,
)
from ..models.IntegrationsCreateResponse import (
    IntegrationsCreateResponse as IntegrationsCreateResponseModel,
)


class Integrations(BaseService):
    def get(self, integration: str) -> IntegrationsGetResponseModel:
        """
        Retrieve
        Parameters:
        ----------
            integration: str
                The integration slug
        """

        url_endpoint = "/v3/integrations/integration"
        headers = {}
        query_params = []
        self._add_required_headers(headers)
        if not integration:
            raise ValueError(
                "Parameter integration is required, cannot be empty or blank."
            )
        query_params.append(
            query_serializer.serialize_query("form", False, "integration", integration)
        )
        final_url = self._url_prefix + url_endpoint + "?" + "&".join(query_params)
        res = self._http.get(final_url, headers, True)
        if res and isinstance(res, dict):
            return IntegrationsGetResponseModel(**res)
        return res

    def update(
        self, integration: str, request_input: IntegrationsUpdateRequestModel = None
    ) -> IntegrationsUpdateResponseModel:
        """
        Update
        Parameters:
        ----------
            integration: str
                The slug of the integration to update
        """

        url_endpoint = "/v3/integrations/integration"
        headers = {"Content-Type": "application/json"}
        query_params = []
        self._add_required_headers(headers)
        if not integration:
            raise ValueError(
                "Parameter integration is required, cannot be empty or blank."
            )
        query_params.append(
            query_serializer.serialize_query("form", False, "integration", integration)
        )
        final_url = self._url_prefix + url_endpoint + "?" + "&".join(query_params)
        res = self._http.put(final_url, headers, request_input, True)
        if res and isinstance(res, dict):
            return IntegrationsUpdateResponseModel(**res)
        return res

    def delete(self, integration: str) -> IntegrationsDeleteResponseModel:
        """
        Delete
        Parameters:
        ----------
            integration: str
                The slug of the integration to delete
        """

        url_endpoint = "/v3/integrations/integration"
        headers = {}
        query_params = []
        self._add_required_headers(headers)
        if not integration:
            raise ValueError(
                "Parameter integration is required, cannot be empty or blank."
            )
        query_params.append(
            query_serializer.serialize_query("form", False, "integration", integration)
        )
        final_url = self._url_prefix + url_endpoint + "?" + "&".join(query_params)
        res = self._http.delete(final_url, headers, True)
        if res and isinstance(res, dict):
            return IntegrationsDeleteResponseModel(**res)
        return res

    def list(self) -> IntegrationsListResponseModel:
        """
        List
        """

        url_endpoint = "/v3/integrations"
        headers = {}
        self._add_required_headers(headers)

        final_url = self._url_prefix + url_endpoint
        res = self._http.get(final_url, headers, True)
        if res and isinstance(res, dict):
            return IntegrationsListResponseModel(**res)
        return res

    def create(
        self, request_input: IntegrationsCreateRequestModel = None
    ) -> IntegrationsCreateResponseModel:
        """
        Create
        """

        url_endpoint = "/v3/integrations"
        headers = {"Content-Type": "application/json"}
        self._add_required_headers(headers)

        final_url = self._url_prefix + url_endpoint
        res = self._http.post(final_url, headers, request_input, True)
        if res and isinstance(res, dict):
            return IntegrationsCreateResponseModel(**res)
        return res

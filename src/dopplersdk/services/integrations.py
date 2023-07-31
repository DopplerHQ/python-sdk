from urllib.parse import quote
from .base import BaseService
from ..models.IntegrationsCreateRequest import (
    IntegrationsCreateRequest as IntegrationsCreateRequestModel,
)
from ..models.IntegrationsCreate200Response import (
    IntegrationsCreate200Response as IntegrationsCreate200ResponseModel,
)
from ..models.IntegrationsGet200Response import (
    IntegrationsGet200Response as IntegrationsGet200ResponseModel,
)
from ..models.IntegrationsUpdateRequest import (
    IntegrationsUpdateRequest as IntegrationsUpdateRequestModel,
)
from ..models.IntegrationsUpdate200Response import (
    IntegrationsUpdate200Response as IntegrationsUpdate200ResponseModel,
)
from ..models.IntegrationsDelete200Response import (
    IntegrationsDelete200Response as IntegrationsDelete200ResponseModel,
)


class Integrations(BaseService):
    def list(self):
        """
        List
        """

        url_endpoint = "/v3/integrations"
        headers = {}
        self._add_required_headers(headers)

        final_url = self._url_prefix + url_endpoint
        res = self._http.get(final_url, headers, True)
        return res

    def create(
        self, request_input: IntegrationsCreateRequestModel = None
    ) -> IntegrationsCreate200ResponseModel:
        """
        Create
        """

        url_endpoint = "/v3/integrations"
        headers = {"Content-type": "application/json"}
        self._add_required_headers(headers)

        final_url = self._url_prefix + url_endpoint
        res = self._http.post(final_url, headers, request_input, True)
        if res and isinstance(res, dict):
            return IntegrationsCreate200ResponseModel(**res)
        return res

    def get(self, integration: str) -> IntegrationsGet200ResponseModel:
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
        if integration:
            query_params.append(f"integration={integration}")
        final_url = self._url_prefix + url_endpoint + "?" + "&".join(query_params)
        res = self._http.get(final_url, headers, True)
        if res and isinstance(res, dict):
            return IntegrationsGet200ResponseModel(**res)
        return res

    def update(
        self, integration: str, request_input: IntegrationsUpdateRequestModel = None
    ) -> IntegrationsUpdate200ResponseModel:
        """
        Update
        Parameters:
        ----------
            integration: str
                The slug of the integration to update
        """

        url_endpoint = "/v3/integrations/integration"
        headers = {"Content-type": "application/json"}
        query_params = []
        self._add_required_headers(headers)
        if not integration:
            raise ValueError(
                "Parameter integration is required, cannot be empty or blank."
            )
        if integration:
            query_params.append(f"integration={integration}")
        final_url = self._url_prefix + url_endpoint + "?" + "&".join(query_params)
        res = self._http.put(final_url, headers, request_input, True)
        if res and isinstance(res, dict):
            return IntegrationsUpdate200ResponseModel(**res)
        return res

    def delete(self, integration: str) -> IntegrationsDelete200ResponseModel:
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
        if integration:
            query_params.append(f"integration={integration}")
        final_url = self._url_prefix + url_endpoint + "?" + "&".join(query_params)
        res = self._http.delete(final_url, headers, True)
        if res and isinstance(res, dict):
            return IntegrationsDelete200ResponseModel(**res)
        return res

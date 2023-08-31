from urllib.parse import quote
from .base import BaseService
from ..models.ListResponse import ListResponse as ListResponseModel
from ..models.CreateRequest import CreateRequest as CreateRequestModel
from ..models.CreateResponse import CreateResponse as CreateResponseModel
from ..models.GetResponse import GetResponse as GetResponseModel
from ..models.UpdateRequest import UpdateRequest as UpdateRequestModel
from ..models.UpdateResponse import UpdateResponse as UpdateResponseModel
from ..models.DeleteResponse import DeleteResponse as DeleteResponseModel


class Integrations(BaseService):
    def list(self) -> ListResponseModel:
        """
        List
        """

        url_endpoint = "/v3/integrations"
        headers = {}
        self._add_required_headers(headers)

        final_url = self._url_prefix + url_endpoint
        res = self._http.get(final_url, headers, True)
        if res and isinstance(res, dict):
            return ListResponseModel(**res)
        return res

    def create(self, request_input: CreateRequestModel = None) -> CreateResponseModel:
        """
        Create
        """

        url_endpoint = "/v3/integrations"
        headers = {"Content-type": "application/json"}
        self._add_required_headers(headers)

        final_url = self._url_prefix + url_endpoint
        res = self._http.post(final_url, headers, request_input, True)
        if res and isinstance(res, dict):
            return CreateResponseModel(**res)
        return res

    def get(self, integration: str) -> GetResponseModel:
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
        query_params.append(f"integration={integration}")
        final_url = self._url_prefix + url_endpoint + "?" + "&".join(query_params)
        res = self._http.get(final_url, headers, True)
        if res and isinstance(res, dict):
            return GetResponseModel(**res)
        return res

    def update(
        self, integration: str, request_input: UpdateRequestModel = None
    ) -> UpdateResponseModel:
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
        query_params.append(f"integration={integration}")
        final_url = self._url_prefix + url_endpoint + "?" + "&".join(query_params)
        res = self._http.put(final_url, headers, request_input, True)
        if res and isinstance(res, dict):
            return UpdateResponseModel(**res)
        return res

    def delete(self, integration: str) -> DeleteResponseModel:
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
        query_params.append(f"integration={integration}")
        final_url = self._url_prefix + url_endpoint + "?" + "&".join(query_params)
        res = self._http.delete(final_url, headers, True)
        if res and isinstance(res, dict):
            return DeleteResponseModel(**res)
        return res

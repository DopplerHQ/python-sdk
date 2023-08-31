from urllib.parse import quote
from .base import BaseService
from ..models.ListResponse import ListResponse as ListResponseModel
from ..models.CreateRequest import CreateRequest as CreateRequestModel
from ..models.CreateResponse import CreateResponse as CreateResponseModel
from ..models.GetResponse import GetResponse as GetResponseModel
from ..models.UpdateRequest import UpdateRequest as UpdateRequestModel
from ..models.UpdateResponse import UpdateResponse as UpdateResponseModel


class ServiceAccounts(BaseService):
    def list(self, page: int = None, per_page: int = None) -> ListResponseModel:
        """
        List
        Parameters:
        ----------
            page: int
            per_page: int
        """

        url_endpoint = "/v3/workplace/service_accounts"
        headers = {}
        query_params = []
        self._add_required_headers(headers)
        if page:
            query_params.append(f"page={page}")
        if per_page:
            query_params.append(f"per_page={per_page}")
        final_url = self._url_prefix + url_endpoint
        if len(query_params) > 0:
            final_url += "?" + "&".join(query_params)
        res = self._http.get(final_url, headers, True)
        if res and isinstance(res, dict):
            return ListResponseModel(**res)
        return res

    def create(self, request_input: CreateRequestModel = None) -> CreateResponseModel:
        """
        Create
        """

        url_endpoint = "/v3/workplace/service_accounts"
        headers = {"Content-type": "application/json"}
        self._add_required_headers(headers)

        final_url = self._url_prefix + url_endpoint
        res = self._http.post(final_url, headers, request_input, True)
        if res and isinstance(res, dict):
            return CreateResponseModel(**res)
        return res

    def get(self, slug: str) -> GetResponseModel:
        """
        Retrieve
        Parameters:
        ----------
            slug: str
                Slug of the service account
        """

        url_endpoint = "/v3/workplace/service_accounts/service_account/{slug}"
        headers = {}
        self._add_required_headers(headers)
        if not slug:
            raise ValueError("Parameter slug is required, cannot be empty or blank.")
        url_endpoint = url_endpoint.replace("{slug}", quote(str(slug)))
        final_url = self._url_prefix + url_endpoint
        res = self._http.get(final_url, headers, True)
        if res and isinstance(res, dict):
            return GetResponseModel(**res)
        return res

    def update(
        self, slug: str, request_input: UpdateRequestModel = None
    ) -> UpdateResponseModel:
        """
        Update
        Parameters:
        ----------
            slug: str
                Slug of the service account
        """

        url_endpoint = "/v3/workplace/service_accounts/service_account/{slug}"
        headers = {"Content-type": "application/json"}
        self._add_required_headers(headers)
        if not slug:
            raise ValueError("Parameter slug is required, cannot be empty or blank.")
        url_endpoint = url_endpoint.replace("{slug}", quote(str(slug)))
        final_url = self._url_prefix + url_endpoint
        res = self._http.patch(final_url, headers, request_input, True)
        if res and isinstance(res, dict):
            return UpdateResponseModel(**res)
        return res

    def delete(self, slug: str):
        """
        Delete
        Parameters:
        ----------
            slug: str
                Slug of the service account
        """

        url_endpoint = "/v3/workplace/service_accounts/service_account/{slug}"
        headers = {}
        self._add_required_headers(headers)
        if not slug:
            raise ValueError("Parameter slug is required, cannot be empty or blank.")
        url_endpoint = url_endpoint.replace("{slug}", quote(str(slug)))
        final_url = self._url_prefix + url_endpoint
        res = self._http.delete(final_url, headers, True)
        return res

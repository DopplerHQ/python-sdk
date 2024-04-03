from urllib.parse import quote
from ..net import query_serializer
from .base import BaseService
from ..models.ServiceAccountsGetResponse import (
    ServiceAccountsGetResponse as ServiceAccountsGetResponseModel,
)
from ..models.ServiceAccountsUpdateRequest import (
    ServiceAccountsUpdateRequest as ServiceAccountsUpdateRequestModel,
)
from ..models.ServiceAccountsUpdateResponse import (
    ServiceAccountsUpdateResponse as ServiceAccountsUpdateResponseModel,
)
from ..models.ServiceAccountsListResponse import (
    ServiceAccountsListResponse as ServiceAccountsListResponseModel,
)
from ..models.ServiceAccountsCreateRequest import (
    ServiceAccountsCreateRequest as ServiceAccountsCreateRequestModel,
)
from ..models.ServiceAccountsCreateResponse import (
    ServiceAccountsCreateResponse as ServiceAccountsCreateResponseModel,
)


class ServiceAccounts(BaseService):
    def get(self, slug: str) -> ServiceAccountsGetResponseModel:
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
        url_endpoint = url_endpoint.replace(
            "{slug}",
            quote(str(query_serializer.serialize_path("simple", False, slug, None))),
        )
        final_url = self._url_prefix + url_endpoint
        res = self._http.get(final_url, headers, True)
        if res and isinstance(res, dict):
            return ServiceAccountsGetResponseModel(**res)
        return res

    def update(
        self, slug: str, request_input: ServiceAccountsUpdateRequestModel = None
    ) -> ServiceAccountsUpdateResponseModel:
        """
        Update
        Parameters:
        ----------
            slug: str
                Slug of the service account
        """

        url_endpoint = "/v3/workplace/service_accounts/service_account/{slug}"
        headers = {"Content-Type": "application/json"}
        self._add_required_headers(headers)
        if not slug:
            raise ValueError("Parameter slug is required, cannot be empty or blank.")
        url_endpoint = url_endpoint.replace(
            "{slug}",
            quote(str(query_serializer.serialize_path("simple", False, slug, None))),
        )
        final_url = self._url_prefix + url_endpoint
        res = self._http.patch(final_url, headers, request_input, True)
        if res and isinstance(res, dict):
            return ServiceAccountsUpdateResponseModel(**res)
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
        url_endpoint = url_endpoint.replace(
            "{slug}",
            quote(str(query_serializer.serialize_path("simple", False, slug, None))),
        )
        final_url = self._url_prefix + url_endpoint
        res = self._http.delete(final_url, headers, True)
        return res

    def list(
        self, page: int = None, per_page: int = None
    ) -> ServiceAccountsListResponseModel:
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
            query_params.append(
                query_serializer.serialize_query("form", False, "page", page)
            )
        if per_page:
            query_params.append(
                query_serializer.serialize_query("form", False, "per_page", per_page)
            )
        final_url = self._url_prefix + url_endpoint
        if len(query_params) > 0:
            final_url += "?" + "&".join(query_params)
        res = self._http.get(final_url, headers, True)
        if res and isinstance(res, dict):
            return ServiceAccountsListResponseModel(**res)
        return res

    def create(
        self, request_input: ServiceAccountsCreateRequestModel = None
    ) -> ServiceAccountsCreateResponseModel:
        """
        Create
        """

        url_endpoint = "/v3/workplace/service_accounts"
        headers = {"Content-Type": "application/json"}
        self._add_required_headers(headers)

        final_url = self._url_prefix + url_endpoint
        res = self._http.post(final_url, headers, request_input, True)
        if res and isinstance(res, dict):
            return ServiceAccountsCreateResponseModel(**res)
        return res

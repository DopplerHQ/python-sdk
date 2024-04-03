from urllib.parse import quote
from ..net import query_serializer
from .base import BaseService
from ..models.ServiceAccountTokensListResponse import (
    ServiceAccountTokensListResponse as ServiceAccountTokensListResponseModel,
)
from ..models.ServiceAccountTokensCreateRequest import (
    ServiceAccountTokensCreateRequest as ServiceAccountTokensCreateRequestModel,
)
from ..models.ServiceAccountTokensCreateResponse import (
    ServiceAccountTokensCreateResponse as ServiceAccountTokensCreateResponseModel,
)
from ..models.ServiceAccountTokensGetResponse import (
    ServiceAccountTokensGetResponse as ServiceAccountTokensGetResponseModel,
)


class ServiceAccountTokens(BaseService):
    def list(
        self, service_account: str, page: int = None, per_page: int = None
    ) -> ServiceAccountTokensListResponseModel:
        """
        List
        Parameters:
        ----------
            page: int
            per_page: int
            service_account: str
                Slug of the service account
        """

        url_endpoint = (
            "/v3/workplace/service_accounts/service_account/{service_account}/tokens"
        )
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
        if not service_account:
            raise ValueError(
                "Parameter service_account is required, cannot be empty or blank."
            )
        url_endpoint = url_endpoint.replace(
            "{service_account}",
            quote(
                str(
                    query_serializer.serialize_path(
                        "simple", False, service_account, None
                    )
                )
            ),
        )
        final_url = self._url_prefix + url_endpoint
        if len(query_params) > 0:
            final_url += "?" + "&".join(query_params)
        res = self._http.get(final_url, headers, True)
        if res and isinstance(res, dict):
            return ServiceAccountTokensListResponseModel(**res)
        return res

    def create(
        self,
        service_account: str,
        request_input: ServiceAccountTokensCreateRequestModel = None,
    ) -> ServiceAccountTokensCreateResponseModel:
        """
        Create
        Parameters:
        ----------
            service_account: str
                Slug of the service account
        """

        url_endpoint = (
            "/v3/workplace/service_accounts/service_account/{service_account}/tokens"
        )
        headers = {"Content-Type": "application/json"}
        self._add_required_headers(headers)
        if not service_account:
            raise ValueError(
                "Parameter service_account is required, cannot be empty or blank."
            )
        url_endpoint = url_endpoint.replace(
            "{service_account}",
            quote(
                str(
                    query_serializer.serialize_path(
                        "simple", False, service_account, None
                    )
                )
            ),
        )
        final_url = self._url_prefix + url_endpoint
        res = self._http.post(final_url, headers, request_input, True)
        if res and isinstance(res, dict):
            return ServiceAccountTokensCreateResponseModel(**res)
        return res

    def get(
        self, api_token: str, service_account: str
    ) -> ServiceAccountTokensGetResponseModel:
        """
        Retrieve
        Parameters:
        ----------
            service_account: str
                Slug of the service account
            api_token: str
                Slug of the API token
        """

        url_endpoint = "/v3/workplace/service_accounts/service_account/{service_account}/tokens/token/{api_token}"
        headers = {}
        self._add_required_headers(headers)
        if not service_account:
            raise ValueError(
                "Parameter service_account is required, cannot be empty or blank."
            )
        url_endpoint = url_endpoint.replace(
            "{service_account}",
            quote(
                str(
                    query_serializer.serialize_path(
                        "simple", False, service_account, None
                    )
                )
            ),
        )
        if not api_token:
            raise ValueError(
                "Parameter api_token is required, cannot be empty or blank."
            )
        url_endpoint = url_endpoint.replace(
            "{api_token}",
            quote(
                str(query_serializer.serialize_path("simple", False, api_token, None))
            ),
        )
        final_url = self._url_prefix + url_endpoint
        res = self._http.get(final_url, headers, True)
        if res and isinstance(res, dict):
            return ServiceAccountTokensGetResponseModel(**res)
        return res

    def delete(self, api_token: str, service_account: str):
        """
        Delete
        Parameters:
        ----------
            service_account: str
                Slug of the service account
            api_token: str
                Slug of the API token
        """

        url_endpoint = "/v3/workplace/service_accounts/service_account/{service_account}/tokens/token/{api_token}"
        headers = {}
        self._add_required_headers(headers)
        if not service_account:
            raise ValueError(
                "Parameter service_account is required, cannot be empty or blank."
            )
        url_endpoint = url_endpoint.replace(
            "{service_account}",
            quote(
                str(
                    query_serializer.serialize_path(
                        "simple", False, service_account, None
                    )
                )
            ),
        )
        if not api_token:
            raise ValueError(
                "Parameter api_token is required, cannot be empty or blank."
            )
        url_endpoint = url_endpoint.replace(
            "{api_token}",
            quote(
                str(query_serializer.serialize_path("simple", False, api_token, None))
            ),
        )
        final_url = self._url_prefix + url_endpoint
        res = self._http.delete(final_url, headers, True)
        return res

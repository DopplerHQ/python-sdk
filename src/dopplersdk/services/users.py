from urllib.parse import quote
from ..net import query_serializer
from .base import BaseService
from ..models.UsersListResponse import UsersListResponse as UsersListResponseModel
from ..models.UsersGetResponse import UsersGetResponse as UsersGetResponseModel


class Users(BaseService):
    def list(self, page: int = None, email: str = None) -> UsersListResponseModel:
        """
        List
        Parameters:
        ----------
            page: int
                The page of users to fetch
            email: str
                Filter results to only include the user with the provided email address
        """

        url_endpoint = "/v3/workplace/users"
        headers = {}
        query_params = []
        self._add_required_headers(headers)
        if page:
            query_params.append(
                query_serializer.serialize_query("form", False, "page", page)
            )
        if email:
            query_params.append(
                query_serializer.serialize_query("form", False, "email", email)
            )
        final_url = self._url_prefix + url_endpoint
        if len(query_params) > 0:
            final_url += "?" + "&".join(query_params)
        res = self._http.get(final_url, headers, True)
        if res and isinstance(res, dict):
            return UsersListResponseModel(**res)
        return res

    def get(self, slug: str) -> UsersGetResponseModel:
        """
        Retrieve
        Parameters:
        ----------
            slug: str
                The slug of the workplace user
        """

        url_endpoint = "/v3/workplace/users/{slug}"
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
            return UsersGetResponseModel(**res)
        return res

from urllib.parse import quote
from .base import BaseService
from ..models.ListResponse import ListResponse as ListResponseModel
from ..models.CreateResponse import CreateResponse as CreateResponseModel
from ..models.ListPermissionsResponse import (
    ListPermissionsResponse as ListPermissionsResponseModel,
)
from ..models.GetResponse import GetResponse as GetResponseModel
from ..models.UpdateResponse import UpdateResponse as UpdateResponseModel


class WorkplaceRoles(BaseService):
    def list(self) -> ListResponseModel:
        """
        List
        """

        url_endpoint = "/v3/workplace/roles"
        headers = {}
        self._add_required_headers(headers)

        final_url = self._url_prefix + url_endpoint
        res = self._http.get(final_url, headers, True)
        if res and isinstance(res, dict):
            return ListResponseModel(**res)
        return res

    def create(self) -> CreateResponseModel:
        """
        Create
        """

        url_endpoint = "/v3/workplace/roles"
        headers = {}
        self._add_required_headers(headers)

        final_url = self._url_prefix + url_endpoint
        res = self._http.post(final_url, headers, {}, True)
        if res and isinstance(res, dict):
            return CreateResponseModel(**res)
        return res

    def list_permissions(self) -> ListPermissionsResponseModel:
        """
        List Permissions
        """

        url_endpoint = "/v3/workplace/permissions"
        headers = {}
        self._add_required_headers(headers)

        final_url = self._url_prefix + url_endpoint
        res = self._http.get(final_url, headers, True)
        if res and isinstance(res, dict):
            return ListPermissionsResponseModel(**res)
        return res

    def get(self, role: str) -> GetResponseModel:
        """
        Retrieve
        Parameters:
        ----------
            role: str
                The role's unique identifier
        """

        url_endpoint = "/v3/workplace/roles/role/{role}"
        headers = {}
        self._add_required_headers(headers)
        if not role:
            raise ValueError("Parameter role is required, cannot be empty or blank.")
        url_endpoint = url_endpoint.replace("{role}", quote(str(role)))
        final_url = self._url_prefix + url_endpoint
        res = self._http.get(final_url, headers, True)
        if res and isinstance(res, dict):
            return GetResponseModel(**res)
        return res

    def update(self, role: str) -> UpdateResponseModel:
        """
        Update
        Parameters:
        ----------
            role: str
                The role's unique identifier
        """

        url_endpoint = "/v3/workplace/roles/role/{role}"
        headers = {}
        self._add_required_headers(headers)
        if not role:
            raise ValueError("Parameter role is required, cannot be empty or blank.")
        url_endpoint = url_endpoint.replace("{role}", quote(str(role)))
        final_url = self._url_prefix + url_endpoint
        res = self._http.patch(final_url, headers, {}, True)
        if res and isinstance(res, dict):
            return UpdateResponseModel(**res)
        return res

    def delete(self, role: str):
        """
        Delete
        Parameters:
        ----------
            role: str
                The role's unique identifier
        """

        url_endpoint = "/v3/workplace/roles/role/{role}"
        headers = {}
        self._add_required_headers(headers)
        if not role:
            raise ValueError("Parameter role is required, cannot be empty or blank.")
        url_endpoint = url_endpoint.replace("{role}", quote(str(role)))
        final_url = self._url_prefix + url_endpoint
        res = self._http.delete(final_url, headers, True)
        return res

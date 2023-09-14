from urllib.parse import quote
from ..net import query_serializer
from .base import BaseService
from ..models.ProjectRolesListResponse import (
    ProjectRolesListResponse as ProjectRolesListResponseModel,
)
from ..models.ProjectRolesCreateResponse import (
    ProjectRolesCreateResponse as ProjectRolesCreateResponseModel,
)
from ..models.ProjectRolesGetResponse import (
    ProjectRolesGetResponse as ProjectRolesGetResponseModel,
)
from ..models.ProjectRolesUpdateResponse import (
    ProjectRolesUpdateResponse as ProjectRolesUpdateResponseModel,
)
from ..models.ProjectRolesListPermissionsResponse import (
    ProjectRolesListPermissionsResponse as ProjectRolesListPermissionsResponseModel,
)


class ProjectRoles(BaseService):
    def list(self) -> ProjectRolesListResponseModel:
        """
        List
        """

        url_endpoint = "/v3/projects/roles"
        headers = {}
        self._add_required_headers(headers)

        final_url = self._url_prefix + url_endpoint
        res = self._http.get(final_url, headers, True)
        if res and isinstance(res, dict):
            return ProjectRolesListResponseModel(**res)
        return res

    def create(self) -> ProjectRolesCreateResponseModel:
        """
        Create
        """

        url_endpoint = "/v3/projects/roles"
        headers = {}
        self._add_required_headers(headers)

        final_url = self._url_prefix + url_endpoint
        res = self._http.post(final_url, headers, {}, True)
        if res and isinstance(res, dict):
            return ProjectRolesCreateResponseModel(**res)
        return res

    def get(self, role: str) -> ProjectRolesGetResponseModel:
        """
        Retrieve
        Parameters:
        ----------
            role: str
                The role's unique identifier
        """

        url_endpoint = "/v3/projects/roles/role/{role}"
        headers = {}
        self._add_required_headers(headers)
        if not role:
            raise ValueError("Parameter role is required, cannot be empty or blank.")
        url_endpoint = url_endpoint.replace(
            "{role}",
            quote(str(query_serializer.serialize_path("simple", False, role, None))),
        )
        final_url = self._url_prefix + url_endpoint
        res = self._http.get(final_url, headers, True)
        if res and isinstance(res, dict):
            return ProjectRolesGetResponseModel(**res)
        return res

    def update(self, role: str) -> ProjectRolesUpdateResponseModel:
        """
        Update
        Parameters:
        ----------
            role: str
                The role's unique identifier
        """

        url_endpoint = "/v3/projects/roles/role/{role}"
        headers = {}
        self._add_required_headers(headers)
        if not role:
            raise ValueError("Parameter role is required, cannot be empty or blank.")
        url_endpoint = url_endpoint.replace(
            "{role}",
            quote(str(query_serializer.serialize_path("simple", False, role, None))),
        )
        final_url = self._url_prefix + url_endpoint
        res = self._http.patch(final_url, headers, {}, True)
        if res and isinstance(res, dict):
            return ProjectRolesUpdateResponseModel(**res)
        return res

    def delete(self, role: str):
        """
        Delete
        Parameters:
        ----------
            role: str
                The role's unique identifier
        """

        url_endpoint = "/v3/projects/roles/role/{role}"
        headers = {}
        self._add_required_headers(headers)
        if not role:
            raise ValueError("Parameter role is required, cannot be empty or blank.")
        url_endpoint = url_endpoint.replace(
            "{role}",
            quote(str(query_serializer.serialize_path("simple", False, role, None))),
        )
        final_url = self._url_prefix + url_endpoint
        res = self._http.delete(final_url, headers, True)
        return res

    def list_permissions(self) -> ProjectRolesListPermissionsResponseModel:
        """
        List Permissions
        """

        url_endpoint = "/v3/projects/permissions"
        headers = {}
        self._add_required_headers(headers)

        final_url = self._url_prefix + url_endpoint
        res = self._http.get(final_url, headers, True)
        if res and isinstance(res, dict):
            return ProjectRolesListPermissionsResponseModel(**res)
        return res

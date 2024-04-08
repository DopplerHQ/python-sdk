from urllib.parse import quote
from ..net import query_serializer
from .base import BaseService
from ..models.WorkplaceRolesListResponse import (
    WorkplaceRolesListResponse as WorkplaceRolesListResponseModel,
)
from ..models.WorkplaceRolesCreateRequest import (
    WorkplaceRolesCreateRequest as WorkplaceRolesCreateRequestModel,
)
from ..models.WorkplaceRolesCreateResponse import (
    WorkplaceRolesCreateResponse as WorkplaceRolesCreateResponseModel,
)
from ..models.WorkplaceRolesGetResponse import (
    WorkplaceRolesGetResponse as WorkplaceRolesGetResponseModel,
)
from ..models.WorkplaceRolesUpdateRequest import (
    WorkplaceRolesUpdateRequest as WorkplaceRolesUpdateRequestModel,
)
from ..models.WorkplaceRolesUpdateResponse import (
    WorkplaceRolesUpdateResponse as WorkplaceRolesUpdateResponseModel,
)
from ..models.ListPermissionsResponse import (
    ListPermissionsResponse as ListPermissionsResponseModel,
)


class WorkplaceRoles(BaseService):
    def list(self) -> WorkplaceRolesListResponseModel:
        """
        List
        """

        url_endpoint = "/v3/workplace/roles"
        headers = {}
        self._add_required_headers(headers)

        final_url = self._url_prefix + url_endpoint
        res = self._http.get(final_url, headers, True)
        if res and isinstance(res, dict):
            return WorkplaceRolesListResponseModel(**res)
        return res

    def create(
        self, request_input: WorkplaceRolesCreateRequestModel = None
    ) -> WorkplaceRolesCreateResponseModel:
        """
        Create
        """

        url_endpoint = "/v3/workplace/roles"
        headers = {"Content-Type": "application/json"}
        self._add_required_headers(headers)

        final_url = self._url_prefix + url_endpoint
        res = self._http.post(final_url, headers, request_input, True)
        if res and isinstance(res, dict):
            return WorkplaceRolesCreateResponseModel(**res)
        return res

    def get(self, role: str) -> WorkplaceRolesGetResponseModel:
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
        url_endpoint = url_endpoint.replace(
            "{role}",
            quote(str(query_serializer.serialize_path("simple", False, role, None))),
        )
        final_url = self._url_prefix + url_endpoint
        res = self._http.get(final_url, headers, True)
        if res and isinstance(res, dict):
            return WorkplaceRolesGetResponseModel(**res)
        return res

    def update(
        self, role: str, request_input: WorkplaceRolesUpdateRequestModel = None
    ) -> WorkplaceRolesUpdateResponseModel:
        """
        Update
        Parameters:
        ----------
            role: str
                The role's unique identifier, which is the initial name the role was given
        """

        url_endpoint = "/v3/workplace/roles/role/{role}"
        headers = {"Content-Type": "application/json"}
        self._add_required_headers(headers)
        if not role:
            raise ValueError("Parameter role is required, cannot be empty or blank.")
        url_endpoint = url_endpoint.replace(
            "{role}",
            quote(str(query_serializer.serialize_path("simple", False, role, None))),
        )
        final_url = self._url_prefix + url_endpoint
        res = self._http.patch(final_url, headers, request_input, True)
        if res and isinstance(res, dict):
            return WorkplaceRolesUpdateResponseModel(**res)
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
        url_endpoint = url_endpoint.replace(
            "{role}",
            quote(str(query_serializer.serialize_path("simple", False, role, None))),
        )
        final_url = self._url_prefix + url_endpoint
        res = self._http.delete(final_url, headers, True)
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

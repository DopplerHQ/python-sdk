from urllib.parse import quote
from ..net import query_serializer
from .base import BaseService
from ..models.GroupsListResponse import GroupsListResponse as GroupsListResponseModel
from ..models.GroupsCreateRequest import GroupsCreateRequest as GroupsCreateRequestModel
from ..models.GroupsCreateResponse import (
    GroupsCreateResponse as GroupsCreateResponseModel,
)
from ..models.GroupsGetResponse import GroupsGetResponse as GroupsGetResponseModel
from ..models.GroupsUpdateRequest import GroupsUpdateRequest as GroupsUpdateRequestModel
from ..models.GroupsUpdateResponse import (
    GroupsUpdateResponse as GroupsUpdateResponseModel,
)
from ..models.AddMemberRequest import AddMemberRequest as AddMemberRequestModel
from ..models.GroupsType import GroupsType as GroupsTypeModel


class Groups(BaseService):
    def list(self, page: int = None, per_page: int = None) -> GroupsListResponseModel:
        """
        List
        Parameters:
        ----------
            page: int
            per_page: int
        """

        url_endpoint = "/v3/workplace/groups"
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
            return GroupsListResponseModel(**res)
        return res

    def create(
        self, request_input: GroupsCreateRequestModel = None
    ) -> GroupsCreateResponseModel:
        """
        Create
        """

        url_endpoint = "/v3/workplace/groups"
        headers = {"Content-type": "application/json"}
        self._add_required_headers(headers)

        final_url = self._url_prefix + url_endpoint
        res = self._http.post(final_url, headers, request_input, True)
        if res and isinstance(res, dict):
            return GroupsCreateResponseModel(**res)
        return res

    def get(self, slug: str) -> GroupsGetResponseModel:
        """
        Retrieve
        Parameters:
        ----------
            slug: str
                The group's slug
        """

        url_endpoint = "/v3/workplace/groups/group/{slug}"
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
            return GroupsGetResponseModel(**res)
        return res

    def update(
        self, slug: str, request_input: GroupsUpdateRequestModel = None
    ) -> GroupsUpdateResponseModel:
        """
        Update
        Parameters:
        ----------
            slug: str
                The group's slug
        """

        url_endpoint = "/v3/workplace/groups/group/{slug}"
        headers = {"Content-type": "application/json"}
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
            return GroupsUpdateResponseModel(**res)
        return res

    def delete(self, slug: str):
        """
        Delete
        Parameters:
        ----------
            slug: str
                The group's slug
        """

        url_endpoint = "/v3/workplace/groups/group/{slug}"
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

    def add_member(self, slug: str, request_input: AddMemberRequestModel = None):
        """
        Add Member
        Parameters:
        ----------
            slug: str
                The group's slug
        """

        url_endpoint = "/v3/workplace/groups/group/{slug}/members"
        headers = {"Content-type": "application/json"}
        self._add_required_headers(headers)
        if not slug:
            raise ValueError("Parameter slug is required, cannot be empty or blank.")
        url_endpoint = url_endpoint.replace(
            "{slug}",
            quote(str(query_serializer.serialize_path("simple", False, slug, None))),
        )
        final_url = self._url_prefix + url_endpoint
        res = self._http.post(final_url, headers, request_input, True)
        return res

    def delete_member(self, member_slug: str, type_: GroupsTypeModel, slug: str):
        """
        Delete Member
        Parameters:
        ----------
            slug: str
                The group's slug
            type: GroupsType
            member_slug: str
                The member's slug
        """

        url_endpoint = "/v3/workplace/groups/group/{slug}/members/{type_}/{member_slug}"
        headers = {}
        self._add_required_headers(headers)
        if not slug:
            raise ValueError("Parameter slug is required, cannot be empty or blank.")
        url_endpoint = url_endpoint.replace(
            "{slug}",
            quote(str(query_serializer.serialize_path("simple", False, slug, None))),
        )
        if not type_:
            raise ValueError("Parameter type_ is required, cannot be empty or blank.")
        validated_type_ = self._enum_matching(type_, GroupsTypeModel.list(), "type_")
        url_endpoint = url_endpoint.replace(
            "{type_}",
            quote(
                str(
                    query_serializer.serialize_path(
                        "simple", False, validated_type_, None
                    )
                )
            ),
        )
        if not member_slug:
            raise ValueError(
                "Parameter member_slug is required, cannot be empty or blank."
            )
        url_endpoint = url_endpoint.replace(
            "{member_slug}",
            quote(
                str(query_serializer.serialize_path("simple", False, member_slug, None))
            ),
        )
        final_url = self._url_prefix + url_endpoint
        res = self._http.delete(final_url, headers, True)
        return res

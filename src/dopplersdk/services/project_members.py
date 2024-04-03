from urllib.parse import quote
from ..net import query_serializer
from .base import BaseService
from ..models.ProjectMembersListResponse import (
    ProjectMembersListResponse as ProjectMembersListResponseModel,
)
from ..models.AddRequest import AddRequest as AddRequestModel
from ..models.AddResponse import AddResponse as AddResponseModel
from ..models.Type import Type as TypeModel
from ..models.ProjectMembersGetResponse import (
    ProjectMembersGetResponse as ProjectMembersGetResponseModel,
)
from ..models.ProjectMembersUpdateRequest import (
    ProjectMembersUpdateRequest as ProjectMembersUpdateRequestModel,
)
from ..models.ProjectMembersUpdateResponse import (
    ProjectMembersUpdateResponse as ProjectMembersUpdateResponseModel,
)


class ProjectMembers(BaseService):
    def list(
        self, project: str, page: int = None, per_page: int = None
    ) -> ProjectMembersListResponseModel:
        """
        List
        Parameters:
        ----------
            project: str
                Project slug
            page: int
            per_page: int
        """

        url_endpoint = "/v3/projects/project/members"
        headers = {}
        query_params = []
        self._add_required_headers(headers)
        if not project:
            raise ValueError("Parameter project is required, cannot be empty or blank.")
        query_params.append(
            query_serializer.serialize_query("form", False, "project", project)
        )
        if page:
            query_params.append(
                query_serializer.serialize_query("form", False, "page", page)
            )
        if per_page:
            query_params.append(
                query_serializer.serialize_query("form", False, "per_page", per_page)
            )
        final_url = self._url_prefix + url_endpoint + "?" + "&".join(query_params)
        res = self._http.get(final_url, headers, True)
        if res and isinstance(res, dict):
            return ProjectMembersListResponseModel(**res)
        return res

    def add(
        self, project: str, request_input: AddRequestModel = None
    ) -> AddResponseModel:
        """
        Add
        Parameters:
        ----------
            project: str
                Project slug
        """

        url_endpoint = "/v3/projects/project/members"
        headers = {"Content-Type": "application/json"}
        query_params = []
        self._add_required_headers(headers)
        if not project:
            raise ValueError("Parameter project is required, cannot be empty or blank.")
        query_params.append(
            query_serializer.serialize_query("form", False, "project", project)
        )
        final_url = self._url_prefix + url_endpoint + "?" + "&".join(query_params)
        res = self._http.post(final_url, headers, request_input, True)
        if res and isinstance(res, dict):
            return AddResponseModel(**res)
        return res

    def get(
        self, slug: str, type_: TypeModel, project: str
    ) -> ProjectMembersGetResponseModel:
        """
        Retrieve
        Parameters:
        ----------
            project: str
                Project slug
            type_: Type
            slug: str
                Member's slug
        """

        url_endpoint = "/v3/projects/project/members/member/{type_}/{slug}"
        headers = {}
        query_params = []
        self._add_required_headers(headers)
        if not project:
            raise ValueError("Parameter project is required, cannot be empty or blank.")
        query_params.append(
            query_serializer.serialize_query("form", False, "project", project)
        )
        if not type_:
            raise ValueError("Parameter type_ is required, cannot be empty or blank.")
        validated_type_ = self._enum_matching(type_, TypeModel.list(), "type_")
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
        if not slug:
            raise ValueError("Parameter slug is required, cannot be empty or blank.")
        url_endpoint = url_endpoint.replace(
            "{slug}",
            quote(str(query_serializer.serialize_path("simple", False, slug, None))),
        )
        final_url = self._url_prefix + url_endpoint + "?" + "&".join(query_params)
        res = self._http.get(final_url, headers, True)
        if res and isinstance(res, dict):
            return ProjectMembersGetResponseModel(**res)
        return res

    def update(
        self,
        project: str,
        slug: str,
        type_: TypeModel,
        request_input: ProjectMembersUpdateRequestModel = None,
    ) -> ProjectMembersUpdateResponseModel:
        """
        Update
        Parameters:
        ----------
            type_: Type
            slug: str
                Member's slug
            project: str
                Project slug
        """

        url_endpoint = "/v3/projects/project/members/member/{type_}/{slug}"
        headers = {"Content-Type": "application/json"}
        query_params = []
        self._add_required_headers(headers)
        if not type_:
            raise ValueError("Parameter type_ is required, cannot be empty or blank.")
        validated_type_ = self._enum_matching(type_, TypeModel.list(), "type_")
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
        if not slug:
            raise ValueError("Parameter slug is required, cannot be empty or blank.")
        url_endpoint = url_endpoint.replace(
            "{slug}",
            quote(str(query_serializer.serialize_path("simple", False, slug, None))),
        )
        if not project:
            raise ValueError("Parameter project is required, cannot be empty or blank.")
        query_params.append(
            query_serializer.serialize_query("form", False, "project", project)
        )
        final_url = self._url_prefix + url_endpoint + "?" + "&".join(query_params)
        res = self._http.patch(final_url, headers, request_input, True)
        if res and isinstance(res, dict):
            return ProjectMembersUpdateResponseModel(**res)
        return res

    def delete(self, project: str, slug: str, type_: TypeModel):
        """
        Delete
        Parameters:
        ----------
            type_: Type
            slug: str
                Member's slug
            project: str
                Project slug
        """

        url_endpoint = "/v3/projects/project/members/member/{type_}/{slug}"
        headers = {}
        query_params = []
        self._add_required_headers(headers)
        if not type_:
            raise ValueError("Parameter type_ is required, cannot be empty or blank.")
        validated_type_ = self._enum_matching(type_, TypeModel.list(), "type_")
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
        if not slug:
            raise ValueError("Parameter slug is required, cannot be empty or blank.")
        url_endpoint = url_endpoint.replace(
            "{slug}",
            quote(str(query_serializer.serialize_path("simple", False, slug, None))),
        )
        if not project:
            raise ValueError("Parameter project is required, cannot be empty or blank.")
        query_params.append(
            query_serializer.serialize_query("form", False, "project", project)
        )
        final_url = self._url_prefix + url_endpoint + "?" + "&".join(query_params)
        res = self._http.delete(final_url, headers, True)
        return res

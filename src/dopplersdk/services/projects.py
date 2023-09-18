from urllib.parse import quote
from ..net import query_serializer
from .base import BaseService
from ..models.ListResponse import ListResponse as ListResponseModel
from ..models.CreateRequest import CreateRequest as CreateRequestModel
from ..models.CreateResponse import CreateResponse as CreateResponseModel
from ..models.ProjectsGetResponse import ProjectsGetResponse as ProjectsGetResponseModel
from ..models.ProjectsUpdateRequest import (
    ProjectsUpdateRequest as ProjectsUpdateRequestModel,
)
from ..models.ProjectsUpdateResponse import (
    ProjectsUpdateResponse as ProjectsUpdateResponseModel,
)
from ..models.DeleteRequest import DeleteRequest as DeleteRequestModel


class Projects(BaseService):
    def list(self, page: int = None, per_page: int = None) -> ListResponseModel:
        """
        List
        Parameters:
        ----------
            page: int
                Page number
            per_page: int
                Items per page
        """

        url_endpoint = "/v3/projects"
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
            return ListResponseModel(**res)
        return res

    def create(self, request_input: CreateRequestModel = None) -> CreateResponseModel:
        """
        Create
        """

        url_endpoint = "/v3/projects"
        headers = {"Content-type": "application/json"}
        self._add_required_headers(headers)

        final_url = self._url_prefix + url_endpoint
        res = self._http.post(final_url, headers, request_input, True)
        if res and isinstance(res, dict):
            return CreateResponseModel(**res)
        return res

    def get(self, project: str) -> ProjectsGetResponseModel:
        """
        Retrieve
        Parameters:
        ----------
            project: str
                Unique identifier for the project object.
        """

        url_endpoint = "/v3/projects/project"
        headers = {}
        query_params = []
        self._add_required_headers(headers)
        if not project:
            raise ValueError("Parameter project is required, cannot be empty or blank.")
        query_params.append(
            query_serializer.serialize_query("form", False, "project", project)
        )
        final_url = self._url_prefix + url_endpoint + "?" + "&".join(query_params)
        res = self._http.get(final_url, headers, True)
        if res and isinstance(res, dict):
            return ProjectsGetResponseModel(**res)
        return res

    def update(
        self, request_input: ProjectsUpdateRequestModel = None
    ) -> ProjectsUpdateResponseModel:
        """
        Update
        """

        url_endpoint = "/v3/projects/project"
        headers = {"Content-type": "application/json"}
        self._add_required_headers(headers)

        final_url = self._url_prefix + url_endpoint
        res = self._http.post(final_url, headers, request_input, True)
        if res and isinstance(res, dict):
            return ProjectsUpdateResponseModel(**res)
        return res

    def delete(self, request_input: DeleteRequestModel = None):
        """
        Delete
        """

        url_endpoint = "/v3/projects/project"
        headers = {"Content-type": "application/json"}
        self._add_required_headers(headers)

        final_url = self._url_prefix + url_endpoint
        res = self._http.delete(final_url, headers, True)
        return res

from urllib.parse import quote
from .base import BaseService
from ..models.ProjectsList200Response import (
    ProjectsList200Response as ProjectsList200ResponseModel,
)
from ..models.ProjectsCreateRequest import (
    ProjectsCreateRequest as ProjectsCreateRequestModel,
)
from ..models.ProjectsCreate200Response import (
    ProjectsCreate200Response as ProjectsCreate200ResponseModel,
)
from ..models.ProjectsGet200Response import (
    ProjectsGet200Response as ProjectsGet200ResponseModel,
)
from ..models.ProjectsUpdateRequest import (
    ProjectsUpdateRequest as ProjectsUpdateRequestModel,
)
from ..models.ProjectsUpdate200Response import (
    ProjectsUpdate200Response as ProjectsUpdate200ResponseModel,
)
from ..models.ProjectsDeleteRequest import (
    ProjectsDeleteRequest as ProjectsDeleteRequestModel,
)


class Projects(BaseService):
    def list(
        self, page: int = None, per_page: int = None
    ) -> ProjectsList200ResponseModel:
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
            query_params.append(f"page={page}")
        if per_page:
            query_params.append(f"per_page={per_page}")
        final_url = self._url_prefix + url_endpoint
        if len(query_params) > 0:
            final_url += "?" + "&".join(query_params)
        res = self._http.get(final_url, headers, True)
        if res and isinstance(res, dict):
            return ProjectsList200ResponseModel(**res)
        return res

    def create(
        self, request_input: ProjectsCreateRequestModel = None
    ) -> ProjectsCreate200ResponseModel:
        """
        Create
        """

        url_endpoint = "/v3/projects"
        headers = {"Content-type": "application/json"}
        self._add_required_headers(headers)

        final_url = self._url_prefix + url_endpoint
        res = self._http.post(final_url, headers, request_input, True)
        if res and isinstance(res, dict):
            return ProjectsCreate200ResponseModel(**res)
        return res

    def get(self, project: str) -> ProjectsGet200ResponseModel:
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
        if project:
            query_params.append(f"project={project}")
        final_url = self._url_prefix + url_endpoint + "?" + "&".join(query_params)
        res = self._http.get(final_url, headers, True)
        if res and isinstance(res, dict):
            return ProjectsGet200ResponseModel(**res)
        return res

    def update(
        self, request_input: ProjectsUpdateRequestModel = None
    ) -> ProjectsUpdate200ResponseModel:
        """
        Update
        """

        url_endpoint = "/v3/projects/project"
        headers = {"Content-type": "application/json"}
        self._add_required_headers(headers)

        final_url = self._url_prefix + url_endpoint
        res = self._http.post(final_url, headers, request_input, True)
        if res and isinstance(res, dict):
            return ProjectsUpdate200ResponseModel(**res)
        return res

    def delete(self, request_input: ProjectsDeleteRequestModel = None):
        """
        Delete
        """

        url_endpoint = "/v3/projects/project"
        headers = {"Content-type": "application/json"}
        self._add_required_headers(headers)

        final_url = self._url_prefix + url_endpoint
        res = self._http.delete(final_url, headers, True)
        return res

from urllib.parse import quote
from .base import BaseService
from ..models.ListResponse import ListResponse as ListResponseModel
from ..models.AddRequest import AddRequest as AddRequestModel
from ..models.AddResponse import AddResponse as AddResponseModel
from ..models.Type import Type as TypeModel
from ..models.GetResponse import GetResponse as GetResponseModel
from ..models.UpdateRequest import UpdateRequest as UpdateRequestModel
from ..models.UpdateResponse import UpdateResponse as UpdateResponseModel


class ProjectMembers(BaseService):
    def list(
        self, project: str, page: int = None, per_page: int = None
    ) -> ListResponseModel:
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
        query_params.append(f"project={project}")
        if page:
            query_params.append(f"page={page}")
        if per_page:
            query_params.append(f"per_page={per_page}")
        final_url = self._url_prefix + url_endpoint + "?" + "&".join(query_params)
        res = self._http.get(final_url, headers, True)
        if res and isinstance(res, dict):
            return ListResponseModel(**res)
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
        headers = {"Content-type": "application/json"}
        query_params = []
        self._add_required_headers(headers)
        if not project:
            raise ValueError("Parameter project is required, cannot be empty or blank.")
        query_params.append(f"project={project}")
        final_url = self._url_prefix + url_endpoint + "?" + "&".join(query_params)
        res = self._http.post(final_url, headers, request_input, True)
        if res and isinstance(res, dict):
            return AddResponseModel(**res)
        return res

    def get(self, slug: str, type_: TypeModel, project: str) -> GetResponseModel:
        """
        Retrieve
        Parameters:
        ----------
            project: str
                Project slug
            type: Type
            slug: str
                Member's slug
        """

        url_endpoint = "/v3/projects/project/members/member/{type_}/{slug}"
        headers = {}
        query_params = []
        self._add_required_headers(headers)
        if not project:
            raise ValueError("Parameter project is required, cannot be empty or blank.")
        query_params.append(f"project={project}")
        if not type_:
            raise ValueError("Parameter type_ is required, cannot be empty or blank.")
        validated_type_ = self._enum_matching(type_, TypeModel.list(), "type_")
        url_endpoint = url_endpoint.replace("{type_}", quote(str(validated_type_)))
        if not slug:
            raise ValueError("Parameter slug is required, cannot be empty or blank.")
        url_endpoint = url_endpoint.replace("{slug}", quote(str(slug)))
        final_url = self._url_prefix + url_endpoint + "?" + "&".join(query_params)
        res = self._http.get(final_url, headers, True)
        if res and isinstance(res, dict):
            return GetResponseModel(**res)
        return res

    def update(
        self,
        project: str,
        slug: str,
        type_: TypeModel,
        request_input: UpdateRequestModel = None,
    ) -> UpdateResponseModel:
        """
        Update
        Parameters:
        ----------
            type: Type
            slug: str
                Member's slug
            project: str
                Project slug
        """

        url_endpoint = "/v3/projects/project/members/member/{type_}/{slug}"
        headers = {"Content-type": "application/json"}
        query_params = []
        self._add_required_headers(headers)
        if not type_:
            raise ValueError("Parameter type_ is required, cannot be empty or blank.")
        validated_type_ = self._enum_matching(type_, TypeModel.list(), "type_")
        url_endpoint = url_endpoint.replace("{type_}", quote(str(validated_type_)))
        if not slug:
            raise ValueError("Parameter slug is required, cannot be empty or blank.")
        url_endpoint = url_endpoint.replace("{slug}", quote(str(slug)))
        if not project:
            raise ValueError("Parameter project is required, cannot be empty or blank.")
        query_params.append(f"project={project}")
        final_url = self._url_prefix + url_endpoint + "?" + "&".join(query_params)
        res = self._http.patch(final_url, headers, request_input, True)
        if res and isinstance(res, dict):
            return UpdateResponseModel(**res)
        return res

    def delete(self, project: str, slug: str, type_: TypeModel):
        """
        Delete
        Parameters:
        ----------
            type: Type
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
        url_endpoint = url_endpoint.replace("{type_}", quote(str(validated_type_)))
        if not slug:
            raise ValueError("Parameter slug is required, cannot be empty or blank.")
        url_endpoint = url_endpoint.replace("{slug}", quote(str(slug)))
        if not project:
            raise ValueError("Parameter project is required, cannot be empty or blank.")
        query_params.append(f"project={project}")
        final_url = self._url_prefix + url_endpoint + "?" + "&".join(query_params)
        res = self._http.delete(final_url, headers, True)
        return res

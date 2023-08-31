from urllib.parse import quote
from .base import BaseService
from ..models.ListResponse import ListResponse as ListResponseModel
from ..models.CreateRequest import CreateRequest as CreateRequestModel
from ..models.CreateResponse import CreateResponse as CreateResponseModel
from ..models.GetResponse import GetResponse as GetResponseModel
from ..models.RenameRequest import RenameRequest as RenameRequestModel
from ..models.RenameResponse import RenameResponse as RenameResponseModel


class Environments(BaseService):
    def list(self, project: str) -> ListResponseModel:
        """
        List
        Parameters:
        ----------
            project: str
                The project's name
        """

        url_endpoint = "/v3/environments"
        headers = {}
        query_params = []
        self._add_required_headers(headers)
        if not project:
            raise ValueError("Parameter project is required, cannot be empty or blank.")
        query_params.append(f"project={project}")
        final_url = self._url_prefix + url_endpoint + "?" + "&".join(query_params)
        res = self._http.get(final_url, headers, True)
        if res and isinstance(res, dict):
            return ListResponseModel(**res)
        return res

    def create(
        self, project: str, request_input: CreateRequestModel = None
    ) -> CreateResponseModel:
        """
        Create
        Parameters:
        ----------
            project: str
                The project's name
        """

        url_endpoint = "/v3/environments"
        headers = {"Content-type": "application/json"}
        query_params = []
        self._add_required_headers(headers)
        if not project:
            raise ValueError("Parameter project is required, cannot be empty or blank.")
        query_params.append(f"project={project}")
        final_url = self._url_prefix + url_endpoint + "?" + "&".join(query_params)
        res = self._http.post(final_url, headers, request_input, True)
        if res and isinstance(res, dict):
            return CreateResponseModel(**res)
        return res

    def get(self, environment: str, project: str) -> GetResponseModel:
        """
        Retrieve
        Parameters:
        ----------
            project: str
                The project's name
            environment: str
                The environment's slug
        """

        url_endpoint = "/v3/environments/environment"
        headers = {}
        query_params = []
        self._add_required_headers(headers)
        if not project:
            raise ValueError("Parameter project is required, cannot be empty or blank.")
        query_params.append(f"project={project}")
        if not environment:
            raise ValueError(
                "Parameter environment is required, cannot be empty or blank."
            )
        query_params.append(f"environment={environment}")
        final_url = self._url_prefix + url_endpoint + "?" + "&".join(query_params)
        res = self._http.get(final_url, headers, True)
        if res and isinstance(res, dict):
            return GetResponseModel(**res)
        return res

    def rename(
        self, environment: str, project: str, request_input: RenameRequestModel = None
    ) -> RenameResponseModel:
        """
        Rename
        Parameters:
        ----------
            project: str
                The project's name
            environment: str
                The environment's slug
        """

        url_endpoint = "/v3/environments/environment"
        headers = {"Content-type": "application/json"}
        query_params = []
        self._add_required_headers(headers)
        if not project:
            raise ValueError("Parameter project is required, cannot be empty or blank.")
        query_params.append(f"project={project}")
        if not environment:
            raise ValueError(
                "Parameter environment is required, cannot be empty or blank."
            )
        query_params.append(f"environment={environment}")
        final_url = self._url_prefix + url_endpoint + "?" + "&".join(query_params)
        res = self._http.put(final_url, headers, request_input, True)
        if res and isinstance(res, dict):
            return RenameResponseModel(**res)
        return res

    def delete(self, environment: str, project: str):
        """
        Delete
        Parameters:
        ----------
            project: str
                The project's name
            environment: str
                The environment's slug
        """

        url_endpoint = "/v3/environments/environment"
        headers = {}
        query_params = []
        self._add_required_headers(headers)
        if not project:
            raise ValueError("Parameter project is required, cannot be empty or blank.")
        query_params.append(f"project={project}")
        if not environment:
            raise ValueError(
                "Parameter environment is required, cannot be empty or blank."
            )
        query_params.append(f"environment={environment}")
        final_url = self._url_prefix + url_endpoint + "?" + "&".join(query_params)
        res = self._http.delete(final_url, headers, True)
        return res

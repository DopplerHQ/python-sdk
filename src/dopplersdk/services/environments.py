from urllib.parse import quote
from .base import BaseService
from ..models.EnvironmentsGet200Response import (
    EnvironmentsGet200Response as EnvironmentsGet200ResponseModel,
)
from ..models.EnvironmentsRenameRequest import (
    EnvironmentsRenameRequest as EnvironmentsRenameRequestModel,
)
from ..models.EnvironmentsRename200Response import (
    EnvironmentsRename200Response as EnvironmentsRename200ResponseModel,
)
from ..models.EnvironmentsList200Response import (
    EnvironmentsList200Response as EnvironmentsList200ResponseModel,
)
from ..models.EnvironmentsCreateRequest import (
    EnvironmentsCreateRequest as EnvironmentsCreateRequestModel,
)
from ..models.EnvironmentsCreate200Response import (
    EnvironmentsCreate200Response as EnvironmentsCreate200ResponseModel,
)


class Environments(BaseService):
    def get(self, environment: str, project: str) -> EnvironmentsGet200ResponseModel:
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
        if project:
            query_params.append(f"project={project}")
        if not environment:
            raise ValueError(
                "Parameter environment is required, cannot be empty or blank."
            )
        if environment:
            query_params.append(f"environment={environment}")
        final_url = self._url_prefix + url_endpoint + "?" + "&".join(query_params)
        res = self._http.get(final_url, headers, True)
        if res and isinstance(res, dict):
            return EnvironmentsGet200ResponseModel(**res)
        return res

    def rename(
        self,
        environment: str,
        project: str,
        request_input: EnvironmentsRenameRequestModel = None,
    ) -> EnvironmentsRename200ResponseModel:
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
        if project:
            query_params.append(f"project={project}")
        if not environment:
            raise ValueError(
                "Parameter environment is required, cannot be empty or blank."
            )
        if environment:
            query_params.append(f"environment={environment}")
        final_url = self._url_prefix + url_endpoint + "?" + "&".join(query_params)
        res = self._http.put(final_url, headers, request_input, True)
        if res and isinstance(res, dict):
            return EnvironmentsRename200ResponseModel(**res)
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
        if project:
            query_params.append(f"project={project}")
        if not environment:
            raise ValueError(
                "Parameter environment is required, cannot be empty or blank."
            )
        if environment:
            query_params.append(f"environment={environment}")
        final_url = self._url_prefix + url_endpoint + "?" + "&".join(query_params)
        res = self._http.delete(final_url, headers, True)
        return res

    def list(self, project: str) -> EnvironmentsList200ResponseModel:
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
        if project:
            query_params.append(f"project={project}")
        final_url = self._url_prefix + url_endpoint + "?" + "&".join(query_params)
        res = self._http.get(final_url, headers, True)
        if res and isinstance(res, dict):
            return EnvironmentsList200ResponseModel(**res)
        return res

    def create(
        self, project: str, request_input: EnvironmentsCreateRequestModel = None
    ) -> EnvironmentsCreate200ResponseModel:
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
        if project:
            query_params.append(f"project={project}")
        final_url = self._url_prefix + url_endpoint + "?" + "&".join(query_params)
        res = self._http.post(final_url, headers, request_input, True)
        if res and isinstance(res, dict):
            return EnvironmentsCreate200ResponseModel(**res)
        return res

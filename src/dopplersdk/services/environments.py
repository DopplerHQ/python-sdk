from urllib.parse import quote
from ..net import query_serializer
from .base import BaseService
from ..models.EnvironmentsListResponse import (
    EnvironmentsListResponse as EnvironmentsListResponseModel,
)
from ..models.EnvironmentsCreateRequest import (
    EnvironmentsCreateRequest as EnvironmentsCreateRequestModel,
)
from ..models.EnvironmentsCreateResponse import (
    EnvironmentsCreateResponse as EnvironmentsCreateResponseModel,
)
from ..models.EnvironmentsGetResponse import (
    EnvironmentsGetResponse as EnvironmentsGetResponseModel,
)
from ..models.RenameRequest import RenameRequest as RenameRequestModel
from ..models.RenameResponse import RenameResponse as RenameResponseModel


class Environments(BaseService):
    def list(self, project: str) -> EnvironmentsListResponseModel:
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
        query_params.append(
            query_serializer.serialize_query("form", False, "project", project)
        )
        final_url = self._url_prefix + url_endpoint + "?" + "&".join(query_params)
        res = self._http.get(final_url, headers, True)
        if res and isinstance(res, dict):
            return EnvironmentsListResponseModel(**res)
        return res

    def create(
        self, project: str, request_input: EnvironmentsCreateRequestModel = None
    ) -> EnvironmentsCreateResponseModel:
        """
        Create
        Parameters:
        ----------
            project: str
                The project's name
        """

        url_endpoint = "/v3/environments"
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
            return EnvironmentsCreateResponseModel(**res)
        return res

    def get(self, environment: str, project: str) -> EnvironmentsGetResponseModel:
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
        query_params.append(
            query_serializer.serialize_query("form", False, "project", project)
        )
        if not environment:
            raise ValueError(
                "Parameter environment is required, cannot be empty or blank."
            )
        query_params.append(
            query_serializer.serialize_query("form", False, "environment", environment)
        )
        final_url = self._url_prefix + url_endpoint + "?" + "&".join(query_params)
        res = self._http.get(final_url, headers, True)
        if res and isinstance(res, dict):
            return EnvironmentsGetResponseModel(**res)
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
        headers = {"Content-Type": "application/json"}
        query_params = []
        self._add_required_headers(headers)
        if not project:
            raise ValueError("Parameter project is required, cannot be empty or blank.")
        query_params.append(
            query_serializer.serialize_query("form", False, "project", project)
        )
        if not environment:
            raise ValueError(
                "Parameter environment is required, cannot be empty or blank."
            )
        query_params.append(
            query_serializer.serialize_query("form", False, "environment", environment)
        )
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
        query_params.append(
            query_serializer.serialize_query("form", False, "project", project)
        )
        if not environment:
            raise ValueError(
                "Parameter environment is required, cannot be empty or blank."
            )
        query_params.append(
            query_serializer.serialize_query("form", False, "environment", environment)
        )
        final_url = self._url_prefix + url_endpoint + "?" + "&".join(query_params)
        res = self._http.delete(final_url, headers, True)
        return res

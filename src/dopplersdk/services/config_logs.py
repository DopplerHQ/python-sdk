from urllib.parse import quote
from ..net import query_serializer
from .base import BaseService
from ..models.ConfigLogsGetResponse import (
    ConfigLogsGetResponse as ConfigLogsGetResponseModel,
)
from ..models.ConfigLogsListResponse import (
    ConfigLogsListResponse as ConfigLogsListResponseModel,
)
from ..models.RollbackResponse import RollbackResponse as RollbackResponseModel


class ConfigLogs(BaseService):
    def get(self, log: str, config: str, project: str) -> ConfigLogsGetResponseModel:
        """
        Retrieve
        Parameters:
        ----------
            project: str
                Unique identifier for the project object.
            config: str
                Name of the config object.
            log: str
                Unique identifier for the log object.
        """

        url_endpoint = "/v3/configs/config/logs/log"
        headers = {}
        query_params = []
        self._add_required_headers(headers)
        if not project:
            raise ValueError("Parameter project is required, cannot be empty or blank.")
        query_params.append(
            query_serializer.serialize_query("form", False, "project", project)
        )
        if not config:
            raise ValueError("Parameter config is required, cannot be empty or blank.")
        query_params.append(
            query_serializer.serialize_query("form", False, "config", config)
        )
        if not log:
            raise ValueError("Parameter log is required, cannot be empty or blank.")
        query_params.append(query_serializer.serialize_query("form", False, "log", log))
        final_url = self._url_prefix + url_endpoint + "?" + "&".join(query_params)
        res = self._http.get(final_url, headers, True)
        if res and isinstance(res, dict):
            return ConfigLogsGetResponseModel(**res)
        return res

    def list(
        self, config: str, project: str, page: int = None, per_page: int = None
    ) -> ConfigLogsListResponseModel:
        """
        List
        Parameters:
        ----------
            project: str
                Unique identifier for the project object.
            config: str
                Name of the config object.
            page: int
                Page number
            per_page: int
                Items per page
        """

        url_endpoint = "/v3/configs/config/logs"
        headers = {}
        query_params = []
        self._add_required_headers(headers)
        if not project:
            raise ValueError("Parameter project is required, cannot be empty or blank.")
        query_params.append(
            query_serializer.serialize_query("form", False, "project", project)
        )
        if not config:
            raise ValueError("Parameter config is required, cannot be empty or blank.")
        query_params.append(
            query_serializer.serialize_query("form", False, "config", config)
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
            return ConfigLogsListResponseModel(**res)
        return res

    def rollback(self, log: str, config: str, project: str) -> RollbackResponseModel:
        """
        Rollback
        Parameters:
        ----------
            project: str
                Unique identifier for the project object.
            config: str
                Name of the config object.
            log: str
                Unique identifier for the log object.
        """

        url_endpoint = "/v3/configs/config/logs/log/rollback"
        headers = {}
        query_params = []
        self._add_required_headers(headers)
        if not project:
            raise ValueError("Parameter project is required, cannot be empty or blank.")
        query_params.append(
            query_serializer.serialize_query("form", False, "project", project)
        )
        if not config:
            raise ValueError("Parameter config is required, cannot be empty or blank.")
        query_params.append(
            query_serializer.serialize_query("form", False, "config", config)
        )
        if not log:
            raise ValueError("Parameter log is required, cannot be empty or blank.")
        query_params.append(query_serializer.serialize_query("form", False, "log", log))
        final_url = self._url_prefix + url_endpoint + "?" + "&".join(query_params)
        res = self._http.post(final_url, headers, {}, True)
        if res and isinstance(res, dict):
            return RollbackResponseModel(**res)
        return res

from urllib.parse import quote
from .base import BaseService
from ..models.ConfigLogsList200Response import (
    ConfigLogsList200Response as ConfigLogsList200ResponseModel,
)
from ..models.ConfigLogsGet200Response import (
    ConfigLogsGet200Response as ConfigLogsGet200ResponseModel,
)
from ..models.ConfigLogsRollback200Response import (
    ConfigLogsRollback200Response as ConfigLogsRollback200ResponseModel,
)


class ConfigLogs(BaseService):
    def list(
        self, config: str, project: str, page: int = None, per_page: int = None
    ) -> ConfigLogsList200ResponseModel:
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
        if project:
            query_params.append(f"project={project}")
        if not config:
            raise ValueError("Parameter config is required, cannot be empty or blank.")
        if config:
            query_params.append(f"config={config}")
        if page:
            query_params.append(f"page={page}")
        if per_page:
            query_params.append(f"per_page={per_page}")
        final_url = self._url_prefix + url_endpoint + "?" + "&".join(query_params)
        res = self._http.get(final_url, headers, True)
        if res and isinstance(res, dict):
            return ConfigLogsList200ResponseModel(**res)
        return res

    def get(self, log: str, config: str, project: str) -> ConfigLogsGet200ResponseModel:
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
        if project:
            query_params.append(f"project={project}")
        if not config:
            raise ValueError("Parameter config is required, cannot be empty or blank.")
        if config:
            query_params.append(f"config={config}")
        if not log:
            raise ValueError("Parameter log is required, cannot be empty or blank.")
        if log:
            query_params.append(f"log={log}")
        final_url = self._url_prefix + url_endpoint + "?" + "&".join(query_params)
        res = self._http.get(final_url, headers, True)
        if res and isinstance(res, dict):
            return ConfigLogsGet200ResponseModel(**res)
        return res

    def rollback(
        self, log: str, config: str, project: str
    ) -> ConfigLogsRollback200ResponseModel:
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
        if project:
            query_params.append(f"project={project}")
        if not config:
            raise ValueError("Parameter config is required, cannot be empty or blank.")
        if config:
            query_params.append(f"config={config}")
        if not log:
            raise ValueError("Parameter log is required, cannot be empty or blank.")
        if log:
            query_params.append(f"log={log}")
        final_url = self._url_prefix + url_endpoint + "?" + "&".join(query_params)
        res = self._http.post(final_url, headers, {}, True)
        if res and isinstance(res, dict):
            return ConfigLogsRollback200ResponseModel(**res)
        return res

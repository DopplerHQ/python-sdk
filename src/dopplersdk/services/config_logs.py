from urllib.parse import quote
from .base import BaseService
from ..models.ListResponse import ListResponse as ListResponseModel
from ..models.GetResponse import GetResponse as GetResponseModel
from ..models.RollbackResponse import RollbackResponse as RollbackResponseModel


class ConfigLogs(BaseService):
    def list(
        self, config: str, project: str, page: int = None, per_page: int = None
    ) -> ListResponseModel:
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
        query_params.append(f"project={project}")
        if not config:
            raise ValueError("Parameter config is required, cannot be empty or blank.")
        query_params.append(f"config={config}")
        if page:
            query_params.append(f"page={page}")
        if per_page:
            query_params.append(f"per_page={per_page}")
        final_url = self._url_prefix + url_endpoint + "?" + "&".join(query_params)
        res = self._http.get(final_url, headers, True)
        if res and isinstance(res, dict):
            return ListResponseModel(**res)
        return res

    def get(self, log: str, config: str, project: str) -> GetResponseModel:
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
        query_params.append(f"project={project}")
        if not config:
            raise ValueError("Parameter config is required, cannot be empty or blank.")
        query_params.append(f"config={config}")
        if not log:
            raise ValueError("Parameter log is required, cannot be empty or blank.")
        query_params.append(f"log={log}")
        final_url = self._url_prefix + url_endpoint + "?" + "&".join(query_params)
        res = self._http.get(final_url, headers, True)
        if res and isinstance(res, dict):
            return GetResponseModel(**res)
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
        query_params.append(f"project={project}")
        if not config:
            raise ValueError("Parameter config is required, cannot be empty or blank.")
        query_params.append(f"config={config}")
        if not log:
            raise ValueError("Parameter log is required, cannot be empty or blank.")
        query_params.append(f"log={log}")
        final_url = self._url_prefix + url_endpoint + "?" + "&".join(query_params)
        res = self._http.post(final_url, headers, {}, True)
        if res and isinstance(res, dict):
            return RollbackResponseModel(**res)
        return res

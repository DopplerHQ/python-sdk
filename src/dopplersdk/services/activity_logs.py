from urllib.parse import quote
from .base import BaseService
from ..models.ListResponse import ListResponse as ListResponseModel
from ..models.RetrieveResponse import RetrieveResponse as RetrieveResponseModel


class ActivityLogs(BaseService):
    def list(self, page: str = None, per_page: int = None) -> ListResponseModel:
        """
        List
        Parameters:
        ----------
            page: str
                Page number
            per_page: int
                Items per page
        """

        url_endpoint = "/v3/logs"
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
            return ListResponseModel(**res)
        return res

    def retrieve(self, log: str) -> RetrieveResponseModel:
        """
        Retrieve
        Parameters:
        ----------
            log: str
                Unique identifier for the log object.
        """

        url_endpoint = "/v3/logs/log"
        headers = {}
        query_params = []
        self._add_required_headers(headers)
        if not log:
            raise ValueError("Parameter log is required, cannot be empty or blank.")
        query_params.append(f"log={log}")
        final_url = self._url_prefix + url_endpoint + "?" + "&".join(query_params)
        res = self._http.get(final_url, headers, True)
        if res and isinstance(res, dict):
            return RetrieveResponseModel(**res)
        return res

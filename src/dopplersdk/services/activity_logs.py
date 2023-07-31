from urllib.parse import quote
from .base import BaseService
from ..models.ActivityLogsRetrieve200Response import (
    ActivityLogsRetrieve200Response as ActivityLogsRetrieve200ResponseModel,
)
from ..models.ActivityLogsList200Response import (
    ActivityLogsList200Response as ActivityLogsList200ResponseModel,
)


class ActivityLogs(BaseService):
    def retrieve(self, log: str) -> ActivityLogsRetrieve200ResponseModel:
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
        if log:
            query_params.append(f"log={log}")
        final_url = self._url_prefix + url_endpoint + "?" + "&".join(query_params)
        res = self._http.get(final_url, headers, True)
        if res and isinstance(res, dict):
            return ActivityLogsRetrieve200ResponseModel(**res)
        return res

    def list(
        self, page: str = None, per_page: int = None
    ) -> ActivityLogsList200ResponseModel:
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
            return ActivityLogsList200ResponseModel(**res)
        return res

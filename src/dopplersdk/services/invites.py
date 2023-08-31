from urllib.parse import quote
from .base import BaseService
from ..models.ListResponse import ListResponse as ListResponseModel


class Invites(BaseService):
    def list(self, page: int = None, per_page: int = None) -> ListResponseModel:
        """
        List
        Parameters:
        ----------
            page: int
            per_page: int
        """

        url_endpoint = "/v3/workplace/invites"
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

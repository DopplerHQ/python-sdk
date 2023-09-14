from urllib.parse import quote
from ..net import query_serializer
from .base import BaseService
from ..models.InvitesListResponse import InvitesListResponse as InvitesListResponseModel


class Invites(BaseService):
    def list(self, page: int = None, per_page: int = None) -> InvitesListResponseModel:
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
            query_params.append(
                query_serializer.serialize_query("form", False, "page", page)
            )
        if per_page:
            query_params.append(
                query_serializer.serialize_query("form", False, "per_page", per_page)
            )
        final_url = self._url_prefix + url_endpoint
        if len(query_params) > 0:
            final_url += "?" + "&".join(query_params)
        res = self._http.get(final_url, headers, True)
        if res and isinstance(res, dict):
            return InvitesListResponseModel(**res)
        return res

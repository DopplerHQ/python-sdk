from urllib.parse import quote

from .base import BaseService
from ..models.MeResponse import MeResponse as MeResponseModel


class V3(BaseService):
    def me(self) -> MeResponseModel:
        """
        Me
        """

        url_endpoint = "/v3/me"
        headers = {}
        self._add_required_headers(headers)

        final_url = self._url_prefix + url_endpoint
        res = self._http.get(final_url, headers, True)
        if res and isinstance(res, dict):
            return MeResponseModel(**res)
        return res

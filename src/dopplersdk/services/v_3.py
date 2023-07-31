from urllib.parse import quote
from .base import BaseService
from ..models.V3Me200Response import V3Me200Response as V3Me200ResponseModel


class V3(BaseService):
    def me(self) -> V3Me200ResponseModel:
        """
        Me
        """

        url_endpoint = "/v3/me"
        headers = {}
        self._add_required_headers(headers)

        final_url = self._url_prefix + url_endpoint
        res = self._http.get(final_url, headers, True)
        if res and isinstance(res, dict):
            return V3Me200ResponseModel(**res)
        return res

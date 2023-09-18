from urllib.parse import quote

from .base import BaseService
from ..models.RevokeRequest import RevokeRequest as RevokeRequestModel
from ..models.MeResponse import MeResponse as MeResponseModel


class Auth(BaseService):
    def revoke(self, request_input: RevokeRequestModel = None):
        """
        Revoke
        """

        url_endpoint = "/v3/auth/revoke"
        headers = {"Content-type": "application/json"}
        self._add_required_headers(headers)

        final_url = self._url_prefix + url_endpoint
        res = self._http.post(final_url, headers, request_input, True)
        return res

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

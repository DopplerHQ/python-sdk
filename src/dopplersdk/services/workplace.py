from urllib.parse import quote

from .base import BaseService
from ..models.WorkplaceGetResponse import (
    WorkplaceGetResponse as WorkplaceGetResponseModel,
)
from ..models.WorkplaceUpdateRequest import (
    WorkplaceUpdateRequest as WorkplaceUpdateRequestModel,
)
from ..models.WorkplaceUpdateResponse import (
    WorkplaceUpdateResponse as WorkplaceUpdateResponseModel,
)


class Workplace(BaseService):
    def get(self) -> WorkplaceGetResponseModel:
        """
        Retrieve
        """

        url_endpoint = "/v3/workplace"
        headers = {}
        self._add_required_headers(headers)

        final_url = self._url_prefix + url_endpoint
        res = self._http.get(final_url, headers, True)
        if res and isinstance(res, dict):
            return WorkplaceGetResponseModel(**res)
        return res

    def update(
        self, request_input: WorkplaceUpdateRequestModel = None
    ) -> WorkplaceUpdateResponseModel:
        """
        Update
        """

        url_endpoint = "/v3/workplace"
        headers = {"Content-Type": "application/json"}
        self._add_required_headers(headers)

        final_url = self._url_prefix + url_endpoint
        res = self._http.post(final_url, headers, request_input, True)
        if res and isinstance(res, dict):
            return WorkplaceUpdateResponseModel(**res)
        return res

from urllib.parse import quote
from ..net import query_serializer
from .base import BaseService
from ..models.OptionsResponse import OptionsResponse as OptionsResponseModel


class Get(BaseService):
    def options(self, integration: str) -> OptionsResponseModel:
        """
        Get Options
        Parameters:
        ----------
            integration: str
                The integration slug
        """

        url_endpoint = "/v3/integrations/integration/options"
        headers = {}
        query_params = []
        self._add_required_headers(headers)
        if not integration:
            raise ValueError(
                "Parameter integration is required, cannot be empty or blank."
            )
        query_params.append(
            query_serializer.serialize_query("form", False, "integration", integration)
        )
        final_url = self._url_prefix + url_endpoint + "?" + "&".join(query_params)
        res = self._http.get(final_url, headers, True)
        if res and isinstance(res, dict):
            return OptionsResponseModel(**res)
        return res

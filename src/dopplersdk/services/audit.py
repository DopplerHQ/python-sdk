from urllib.parse import quote
from ..net import query_serializer
from .base import BaseService
from ..models.GetUserResponse import GetUserResponse as GetUserResponseModel


class Audit(BaseService):
    def get_user(
        self, workplace_user_id: str, settings: bool = None
    ) -> GetUserResponseModel:
        """
        Workplace User
        Parameters:
        ----------
            workplace_user_id: str
                The ID of the workplace user
            settings: bool
                If true, the api will return more information if the user has e.g. SAML enabled and/or Multi Factor Auth enabled
        """

        url_endpoint = "/v3/workplace/users/{workplace_user_id}"
        headers = {}
        query_params = []
        self._add_required_headers(headers)
        if not workplace_user_id:
            raise ValueError(
                "Parameter workplace_user_id is required, cannot be empty or blank."
            )
        url_endpoint = url_endpoint.replace(
            "{workplace_user_id}",
            quote(
                str(
                    query_serializer.serialize_path(
                        "simple", False, workplace_user_id, None
                    )
                )
            ),
        )
        if settings:
            query_params.append(
                query_serializer.serialize_query("form", False, "settings", settings)
            )
        final_url = self._url_prefix + url_endpoint
        if len(query_params) > 0:
            final_url += "?" + "&".join(query_params)
        res = self._http.get(final_url, headers, True)
        if res and isinstance(res, dict):
            return GetUserResponseModel(**res)
        return res

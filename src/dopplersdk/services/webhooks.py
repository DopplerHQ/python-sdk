from urllib.parse import quote
from ..net import query_serializer
from .base import BaseService
from ..models.WebhooksListResponse import (
    WebhooksListResponse as WebhooksListResponseModel,
)
from ..models.WebhooksAddRequest import WebhooksAddRequest as WebhooksAddRequestModel
from ..models.WebhooksAddResponse import WebhooksAddResponse as WebhooksAddResponseModel
from ..models.WebhooksGetResponse import WebhooksGetResponse as WebhooksGetResponseModel
from ..models.WebhooksUpdateRequest import (
    WebhooksUpdateRequest as WebhooksUpdateRequestModel,
)
from ..models.WebhooksUpdateResponse import (
    WebhooksUpdateResponse as WebhooksUpdateResponseModel,
)
from ..models.WebhooksDeleteResponse import (
    WebhooksDeleteResponse as WebhooksDeleteResponseModel,
)
from ..models.EnableResponse import EnableResponse as EnableResponseModel
from ..models.DisableResponse import DisableResponse as DisableResponseModel


class Webhooks(BaseService):
    def list(self, project: str = None) -> WebhooksListResponseModel:
        """
        List
        Parameters:
        ----------
            project: str
                The project's name
        """

        url_endpoint = "/v3/webhooks"
        headers = {}
        query_params = []
        self._add_required_headers(headers)
        if project:
            query_params.append(
                query_serializer.serialize_query("form", False, "project", project)
            )
        final_url = self._url_prefix + url_endpoint
        if len(query_params) > 0:
            final_url += "?" + "&".join(query_params)
        res = self._http.get(final_url, headers, True)
        if res and isinstance(res, dict):
            return WebhooksListResponseModel(**res)
        return res

    def add(
        self, project: str = None, request_input: WebhooksAddRequestModel = None
    ) -> WebhooksAddResponseModel:
        """
        Add
        Parameters:
        ----------
            project: str
                The project's name
        """

        url_endpoint = "/v3/webhooks"
        headers = {"Content-Type": "application/json"}
        query_params = []
        self._add_required_headers(headers)
        if project:
            query_params.append(
                query_serializer.serialize_query("form", False, "project", project)
            )
        final_url = self._url_prefix + url_endpoint
        if len(query_params) > 0:
            final_url += "?" + "&".join(query_params)
        res = self._http.post(final_url, headers, request_input, True)
        if res and isinstance(res, dict):
            return WebhooksAddResponseModel(**res)
        return res

    def get(self, slug: str, project: str = None) -> WebhooksGetResponseModel:
        """
        Retrieve
        Parameters:
        ----------
            slug: str
                Webhook's slug
            project: str
                The project's name
        """

        url_endpoint = "/v3/webhooks/webhook/{slug}"
        headers = {}
        query_params = []
        self._add_required_headers(headers)
        if not slug:
            raise ValueError("Parameter slug is required, cannot be empty or blank.")
        url_endpoint = url_endpoint.replace(
            "{slug}",
            quote(str(query_serializer.serialize_path("simple", False, slug, None))),
        )
        if project:
            query_params.append(
                query_serializer.serialize_query("form", False, "project", project)
            )
        final_url = self._url_prefix + url_endpoint
        if len(query_params) > 0:
            final_url += "?" + "&".join(query_params)
        res = self._http.get(final_url, headers, True)
        if res and isinstance(res, dict):
            return WebhooksGetResponseModel(**res)
        return res

    def update(
        self,
        slug: str,
        project: str = None,
        request_input: WebhooksUpdateRequestModel = None,
    ) -> WebhooksUpdateResponseModel:
        """
        Update
        Parameters:
        ----------
            project: str
                The project's name
            slug: str
                Webhook's slug
        """

        url_endpoint = "/v3/webhooks/webhook/{slug}"
        headers = {"Content-Type": "application/json"}
        query_params = []
        self._add_required_headers(headers)
        if project:
            query_params.append(
                query_serializer.serialize_query("form", False, "project", project)
            )
        if not slug:
            raise ValueError("Parameter slug is required, cannot be empty or blank.")
        url_endpoint = url_endpoint.replace(
            "{slug}",
            quote(str(query_serializer.serialize_path("simple", False, slug, None))),
        )
        final_url = self._url_prefix + url_endpoint
        if len(query_params) > 0:
            final_url += "?" + "&".join(query_params)
        res = self._http.patch(final_url, headers, request_input, True)
        if res and isinstance(res, dict):
            return WebhooksUpdateResponseModel(**res)
        return res

    def delete(self, slug: str, project: str = None) -> WebhooksDeleteResponseModel:
        """
        Delete
        Parameters:
        ----------
            project: str
                The project's name
            slug: str
                Webhook's slug
        """

        url_endpoint = "/v3/webhooks/webhook/{slug}"
        headers = {}
        query_params = []
        self._add_required_headers(headers)
        if project:
            query_params.append(
                query_serializer.serialize_query("form", False, "project", project)
            )
        if not slug:
            raise ValueError("Parameter slug is required, cannot be empty or blank.")
        url_endpoint = url_endpoint.replace(
            "{slug}",
            quote(str(query_serializer.serialize_path("simple", False, slug, None))),
        )
        final_url = self._url_prefix + url_endpoint
        if len(query_params) > 0:
            final_url += "?" + "&".join(query_params)
        res = self._http.delete(final_url, headers, True)
        if res and isinstance(res, dict):
            return WebhooksDeleteResponseModel(**res)
        return res

    def enable(self, slug: str, project: str = None) -> EnableResponseModel:
        """
        Enable
        Parameters:
        ----------
            project: str
                The project's name
            slug: str
                Webhook's slug
        """

        url_endpoint = "/v3/webhooks/webhook/{slug}/enable"
        headers = {}
        query_params = []
        self._add_required_headers(headers)
        if project:
            query_params.append(
                query_serializer.serialize_query("form", False, "project", project)
            )
        if not slug:
            raise ValueError("Parameter slug is required, cannot be empty or blank.")
        url_endpoint = url_endpoint.replace(
            "{slug}",
            quote(str(query_serializer.serialize_path("simple", False, slug, None))),
        )
        final_url = self._url_prefix + url_endpoint
        if len(query_params) > 0:
            final_url += "?" + "&".join(query_params)
        res = self._http.post(final_url, headers, {}, True)
        if res and isinstance(res, dict):
            return EnableResponseModel(**res)
        return res

    def disable(self, slug: str, project: str = None) -> DisableResponseModel:
        """
        Disable
        Parameters:
        ----------
            project: str
                The project's name
            slug: str
                Webhook's slug
        """

        url_endpoint = "/v3/webhooks/webhook/{slug}/disable"
        headers = {}
        query_params = []
        self._add_required_headers(headers)
        if project:
            query_params.append(
                query_serializer.serialize_query("form", False, "project", project)
            )
        if not slug:
            raise ValueError("Parameter slug is required, cannot be empty or blank.")
        url_endpoint = url_endpoint.replace(
            "{slug}",
            quote(str(query_serializer.serialize_path("simple", False, slug, None))),
        )
        final_url = self._url_prefix + url_endpoint
        if len(query_params) > 0:
            final_url += "?" + "&".join(query_params)
        res = self._http.post(final_url, headers, {}, True)
        if res and isinstance(res, dict):
            return DisableResponseModel(**res)
        return res

from urllib.parse import quote
from ..net import query_serializer
from .base import BaseService
from ..models.SyncsCreateRequest import SyncsCreateRequest as SyncsCreateRequestModel
from ..models.SyncsCreateResponse import SyncsCreateResponse as SyncsCreateResponseModel
from ..models.SyncsGetResponse import SyncsGetResponse as SyncsGetResponseModel
from ..models.SyncsDeleteResponse import SyncsDeleteResponse as SyncsDeleteResponseModel


class Syncs(BaseService):
    def create(
        self, config: str, project: str, request_input: SyncsCreateRequestModel = None
    ) -> SyncsCreateResponseModel:
        """
        Create
        Parameters:
        ----------
            project: str
                The project slug
            config: str
                The config slug
        """

        url_endpoint = "/v3/configs/config/syncs"
        headers = {"Content-Type": "application/json"}
        query_params = []
        self._add_required_headers(headers)
        if not project:
            raise ValueError("Parameter project is required, cannot be empty or blank.")
        query_params.append(
            query_serializer.serialize_query("form", False, "project", project)
        )
        if not config:
            raise ValueError("Parameter config is required, cannot be empty or blank.")
        query_params.append(
            query_serializer.serialize_query("form", False, "config", config)
        )
        final_url = self._url_prefix + url_endpoint + "?" + "&".join(query_params)
        res = self._http.post(final_url, headers, request_input, True)
        if res and isinstance(res, dict):
            return SyncsCreateResponseModel(**res)
        return res

    def get(self, sync: str, config: str, project: str) -> SyncsGetResponseModel:
        """
        Retrieve
        Parameters:
        ----------
            project: str
                The project slug
            config: str
                The config slug
            sync: str
                The sync slug
        """

        url_endpoint = "/v3/configs/config/syncs/sync"
        headers = {}
        query_params = []
        self._add_required_headers(headers)
        if not project:
            raise ValueError("Parameter project is required, cannot be empty or blank.")
        query_params.append(
            query_serializer.serialize_query("form", False, "project", project)
        )
        if not config:
            raise ValueError("Parameter config is required, cannot be empty or blank.")
        query_params.append(
            query_serializer.serialize_query("form", False, "config", config)
        )
        if not sync:
            raise ValueError("Parameter sync is required, cannot be empty or blank.")
        query_params.append(
            query_serializer.serialize_query("form", False, "sync", sync)
        )
        final_url = self._url_prefix + url_endpoint + "?" + "&".join(query_params)
        res = self._http.get(final_url, headers, True)
        if res and isinstance(res, dict):
            return SyncsGetResponseModel(**res)
        return res

    def delete(
        self, delete_from_target: bool, sync: str, config: str, project: str
    ) -> SyncsDeleteResponseModel:
        """
        Delete
        Parameters:
        ----------
            project: str
                The project slug
            config: str
                The config slug
            sync: str
                The sync slug
            delete_from_target: bool
                Whether or not to delete the synced data from the target integration
        """

        url_endpoint = "/v3/configs/config/syncs/sync"
        headers = {}
        query_params = []
        self._add_required_headers(headers)
        if not project:
            raise ValueError("Parameter project is required, cannot be empty or blank.")
        query_params.append(
            query_serializer.serialize_query("form", False, "project", project)
        )
        if not config:
            raise ValueError("Parameter config is required, cannot be empty or blank.")
        query_params.append(
            query_serializer.serialize_query("form", False, "config", config)
        )
        if not sync:
            raise ValueError("Parameter sync is required, cannot be empty or blank.")
        query_params.append(
            query_serializer.serialize_query("form", False, "sync", sync)
        )
        if not delete_from_target:
            raise ValueError(
                "Parameter delete_from_target is required, cannot be empty or blank."
            )
        query_params.append(
            query_serializer.serialize_query(
                "form", False, "delete_from_target", delete_from_target
            )
        )
        final_url = self._url_prefix + url_endpoint + "?" + "&".join(query_params)
        res = self._http.delete(final_url, headers, True)
        if res and isinstance(res, dict):
            return SyncsDeleteResponseModel(**res)
        return res

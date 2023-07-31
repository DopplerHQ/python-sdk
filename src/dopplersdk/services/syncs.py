from urllib.parse import quote
from .base import BaseService
from ..models.SyncsCreateRequest import SyncsCreateRequest as SyncsCreateRequestModel
from ..models.SyncsCreate200Response import (
    SyncsCreate200Response as SyncsCreate200ResponseModel,
)
from ..models.SyncsGet200Response import SyncsGet200Response as SyncsGet200ResponseModel
from ..models.SyncsDelete200Response import (
    SyncsDelete200Response as SyncsDelete200ResponseModel,
)


class Syncs(BaseService):
    def create(
        self, config: str, project: str, request_input: SyncsCreateRequestModel = None
    ) -> SyncsCreate200ResponseModel:
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
        headers = {"Content-type": "application/json"}
        query_params = []
        self._add_required_headers(headers)
        if not project:
            raise ValueError("Parameter project is required, cannot be empty or blank.")
        if project:
            query_params.append(f"project={project}")
        if not config:
            raise ValueError("Parameter config is required, cannot be empty or blank.")
        if config:
            query_params.append(f"config={config}")
        final_url = self._url_prefix + url_endpoint + "?" + "&".join(query_params)
        res = self._http.post(final_url, headers, request_input, True)
        if res and isinstance(res, dict):
            return SyncsCreate200ResponseModel(**res)
        return res

    def get(self, sync: str, config: str, project: str) -> SyncsGet200ResponseModel:
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
        if project:
            query_params.append(f"project={project}")
        if not config:
            raise ValueError("Parameter config is required, cannot be empty or blank.")
        if config:
            query_params.append(f"config={config}")
        if not sync:
            raise ValueError("Parameter sync is required, cannot be empty or blank.")
        if sync:
            query_params.append(f"sync={sync}")
        final_url = self._url_prefix + url_endpoint + "?" + "&".join(query_params)
        res = self._http.get(final_url, headers, True)
        if res and isinstance(res, dict):
            return SyncsGet200ResponseModel(**res)
        return res

    def delete(
        self, delete_from_target: bool, sync: str, config: str, project: str
    ) -> SyncsDelete200ResponseModel:
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
        if project:
            query_params.append(f"project={project}")
        if not config:
            raise ValueError("Parameter config is required, cannot be empty or blank.")
        if config:
            query_params.append(f"config={config}")
        if not sync:
            raise ValueError("Parameter sync is required, cannot be empty or blank.")
        if sync:
            query_params.append(f"sync={sync}")
        if not delete_from_target:
            raise ValueError(
                "Parameter delete_from_target is required, cannot be empty or blank."
            )
        if delete_from_target:
            query_params.append(f"delete_from_target={delete_from_target}")
        final_url = self._url_prefix + url_endpoint + "?" + "&".join(query_params)
        res = self._http.delete(final_url, headers, True)
        if res and isinstance(res, dict):
            return SyncsDelete200ResponseModel(**res)
        return res

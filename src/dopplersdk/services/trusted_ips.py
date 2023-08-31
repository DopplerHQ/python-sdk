from urllib.parse import quote
from .base import BaseService
from ..models.ListResponse import ListResponse as ListResponseModel
from ..models.AddRequest import AddRequest as AddRequestModel
from ..models.AddResponse import AddResponse as AddResponseModel
from ..models.DeleteRequest import DeleteRequest as DeleteRequestModel


class TrustedIps(BaseService):
    def list(self, config: str, project: str) -> ListResponseModel:
        """
        List
        Parameters:
        ----------
            project: str
            config: str
        """

        url_endpoint = "/v3/configs/config/trusted_ips"
        headers = {}
        query_params = []
        self._add_required_headers(headers)
        if not project:
            raise ValueError("Parameter project is required, cannot be empty or blank.")
        query_params.append(f"project={project}")
        if not config:
            raise ValueError("Parameter config is required, cannot be empty or blank.")
        query_params.append(f"config={config}")
        final_url = self._url_prefix + url_endpoint + "?" + "&".join(query_params)
        res = self._http.get(final_url, headers, True)
        if res and isinstance(res, dict):
            return ListResponseModel(**res)
        return res

    def add(
        self, config: str, project: str, request_input: AddRequestModel = None
    ) -> AddResponseModel:
        """
        Add
        Parameters:
        ----------
            project: str
            config: str
        """

        url_endpoint = "/v3/configs/config/trusted_ips"
        headers = {"Content-type": "application/json"}
        query_params = []
        self._add_required_headers(headers)
        if not project:
            raise ValueError("Parameter project is required, cannot be empty or blank.")
        query_params.append(f"project={project}")
        if not config:
            raise ValueError("Parameter config is required, cannot be empty or blank.")
        query_params.append(f"config={config}")
        final_url = self._url_prefix + url_endpoint + "?" + "&".join(query_params)
        res = self._http.post(final_url, headers, request_input, True)
        if res and isinstance(res, dict):
            return AddResponseModel(**res)
        return res

    def delete(
        self, config: str, project: str, request_input: DeleteRequestModel = None
    ):
        """
        Delete
        Parameters:
        ----------
            project: str
            config: str
        """

        url_endpoint = "/v3/configs/config/trusted_ips"
        headers = {"Content-type": "application/json"}
        query_params = []
        self._add_required_headers(headers)
        if not project:
            raise ValueError("Parameter project is required, cannot be empty or blank.")
        query_params.append(f"project={project}")
        if not config:
            raise ValueError("Parameter config is required, cannot be empty or blank.")
        query_params.append(f"config={config}")
        final_url = self._url_prefix + url_endpoint + "?" + "&".join(query_params)
        res = self._http.delete(final_url, headers, True)
        return res

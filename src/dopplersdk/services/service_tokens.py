from urllib.parse import quote
from .base import BaseService
from ..models.ListResponse import ListResponse as ListResponseModel
from ..models.CreateRequest import CreateRequest as CreateRequestModel
from ..models.CreateResponse import CreateResponse as CreateResponseModel
from ..models.DeleteRequest import DeleteRequest as DeleteRequestModel
from ..models.DeleteResponse import DeleteResponse as DeleteResponseModel


class ServiceTokens(BaseService):
    def list(self, config: str, project: str) -> ListResponseModel:
        """
        List
        Parameters:
        ----------
            project: str
                Unique identifier for the project object.
            config: str
                Name of the config object.
        """

        url_endpoint = "/v3/configs/config/tokens"
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

    def create(self, request_input: CreateRequestModel = None) -> CreateResponseModel:
        """
        Create
        """

        url_endpoint = "/v3/configs/config/tokens"
        headers = {"Content-type": "application/json"}
        self._add_required_headers(headers)

        final_url = self._url_prefix + url_endpoint
        res = self._http.post(final_url, headers, request_input, True)
        if res and isinstance(res, dict):
            return CreateResponseModel(**res)
        return res

    def delete(self, request_input: DeleteRequestModel = None) -> DeleteResponseModel:
        """
        Delete
        """

        url_endpoint = "/v3/configs/config/tokens/token"
        headers = {"Content-type": "application/json"}
        self._add_required_headers(headers)

        final_url = self._url_prefix + url_endpoint
        res = self._http.delete(final_url, headers, True)
        if res and isinstance(res, dict):
            return DeleteResponseModel(**res)
        return res

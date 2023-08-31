from urllib.parse import quote
from .base import BaseService
from ..models.ListResponse import ListResponse as ListResponseModel
from ..models.CreateRequest import CreateRequest as CreateRequestModel
from ..models.CreateResponse import CreateResponse as CreateResponseModel
from ..models.GetResponse import GetResponse as GetResponseModel
from ..models.UpdateRequest import UpdateRequest as UpdateRequestModel
from ..models.UpdateResponse import UpdateResponse as UpdateResponseModel
from ..models.DeleteRequest import DeleteRequest as DeleteRequestModel
from ..models.DeleteResponse import DeleteResponse as DeleteResponseModel
from ..models.CloneRequest import CloneRequest as CloneRequestModel
from ..models.CloneResponse import CloneResponse as CloneResponseModel
from ..models.LockRequest import LockRequest as LockRequestModel
from ..models.LockResponse import LockResponse as LockResponseModel
from ..models.UnlockRequest import UnlockRequest as UnlockRequestModel
from ..models.UnlockResponse import UnlockResponse as UnlockResponseModel


class Configs(BaseService):
    def list(
        self,
        project: str,
        environment: str = None,
        page: int = None,
        per_page: int = None,
    ) -> ListResponseModel:
        """
        List
        Parameters:
        ----------
            project: str
                The project's name
            environment: str
                (optional) the environment from which to list configs
            page: int
                Page number
            per_page: int
                Items per page
        """

        url_endpoint = "/v3/configs"
        headers = {}
        query_params = []
        self._add_required_headers(headers)
        if not project:
            raise ValueError("Parameter project is required, cannot be empty or blank.")
        query_params.append(f"project={project}")
        if environment:
            query_params.append(f"environment={environment}")
        if page:
            query_params.append(f"page={page}")
        if per_page:
            query_params.append(f"per_page={per_page}")
        final_url = self._url_prefix + url_endpoint + "?" + "&".join(query_params)
        res = self._http.get(final_url, headers, True)
        if res and isinstance(res, dict):
            return ListResponseModel(**res)
        return res

    def create(self, request_input: CreateRequestModel = None) -> CreateResponseModel:
        """
        Create
        """

        url_endpoint = "/v3/configs"
        headers = {"Content-type": "application/json"}
        self._add_required_headers(headers)

        final_url = self._url_prefix + url_endpoint
        res = self._http.post(final_url, headers, request_input, True)
        if res and isinstance(res, dict):
            return CreateResponseModel(**res)
        return res

    def get(self, config: str, project: str) -> GetResponseModel:
        """
        Retrieve
        Parameters:
        ----------
            project: str
                Unique identifier for the project object.
            config: str
                Name of the config object.
        """

        url_endpoint = "/v3/configs/config"
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
            return GetResponseModel(**res)
        return res

    def update(self, request_input: UpdateRequestModel = None) -> UpdateResponseModel:
        """
        Update
        """

        url_endpoint = "/v3/configs/config"
        headers = {"Content-type": "application/json"}
        self._add_required_headers(headers)

        final_url = self._url_prefix + url_endpoint
        res = self._http.post(final_url, headers, request_input, True)
        if res and isinstance(res, dict):
            return UpdateResponseModel(**res)
        return res

    def delete(self, request_input: DeleteRequestModel = None) -> DeleteResponseModel:
        """
        Delete
        """

        url_endpoint = "/v3/configs/config"
        headers = {"Content-type": "application/json"}
        self._add_required_headers(headers)

        final_url = self._url_prefix + url_endpoint
        res = self._http.delete(final_url, headers, True)
        if res and isinstance(res, dict):
            return DeleteResponseModel(**res)
        return res

    def clone(self, request_input: CloneRequestModel = None) -> CloneResponseModel:
        """
        Clone
        """

        url_endpoint = "/v3/configs/config/clone"
        headers = {"Content-type": "application/json"}
        self._add_required_headers(headers)

        final_url = self._url_prefix + url_endpoint
        res = self._http.post(final_url, headers, request_input, True)
        if res and isinstance(res, dict):
            return CloneResponseModel(**res)
        return res

    def lock(self, request_input: LockRequestModel = None) -> LockResponseModel:
        """
        Lock
        """

        url_endpoint = "/v3/configs/config/lock"
        headers = {"Content-type": "application/json"}
        self._add_required_headers(headers)

        final_url = self._url_prefix + url_endpoint
        res = self._http.post(final_url, headers, request_input, True)
        if res and isinstance(res, dict):
            return LockResponseModel(**res)
        return res

    def unlock(self, request_input: UnlockRequestModel = None) -> UnlockResponseModel:
        """
        Unlock
        """

        url_endpoint = "/v3/configs/config/unlock"
        headers = {"Content-type": "application/json"}
        self._add_required_headers(headers)

        final_url = self._url_prefix + url_endpoint
        res = self._http.post(final_url, headers, request_input, True)
        if res and isinstance(res, dict):
            return UnlockResponseModel(**res)
        return res

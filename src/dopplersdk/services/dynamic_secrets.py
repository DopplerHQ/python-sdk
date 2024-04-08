from urllib.parse import quote

from .base import BaseService
from ..models.RevokeLeaseRequest import RevokeLeaseRequest as RevokeLeaseRequestModel
from ..models.RevokeLeaseResponse import RevokeLeaseResponse as RevokeLeaseResponseModel
from ..models.IssueLeaseRequest import IssueLeaseRequest as IssueLeaseRequestModel
from ..models.IssueLeaseResponse import IssueLeaseResponse as IssueLeaseResponseModel


class DynamicSecrets(BaseService):
    def revoke_lease(
        self, request_input: RevokeLeaseRequestModel = None
    ) -> RevokeLeaseResponseModel:
        """
        Revoke Lease
        """

        url_endpoint = "/v3/configs/config/dynamic_secrets/dynamic_secret/leases/lease"
        headers = {"Content-Type": "application/json"}
        self._add_required_headers(headers)

        final_url = self._url_prefix + url_endpoint
        res = self._http.delete(final_url, headers, True)
        if res and isinstance(res, dict):
            return RevokeLeaseResponseModel(**res)
        return res

    def issue_lease(
        self, request_input: IssueLeaseRequestModel = None
    ) -> IssueLeaseResponseModel:
        """
        Issue Lease
        """

        url_endpoint = "/v3/configs/config/dynamic_secrets/dynamic_secret/leases"
        headers = {"Content-Type": "application/json"}
        self._add_required_headers(headers)

        final_url = self._url_prefix + url_endpoint
        res = self._http.post(final_url, headers, request_input, True)
        if res and isinstance(res, dict):
            return IssueLeaseResponseModel(**res)
        return res

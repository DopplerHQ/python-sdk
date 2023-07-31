from urllib.parse import quote
from .base import BaseService
from ..models.DynamicSecretsIssueLeaseRequest import (
    DynamicSecretsIssueLeaseRequest as DynamicSecretsIssueLeaseRequestModel,
)
from ..models.DynamicSecretsRevokeLeaseRequest import (
    DynamicSecretsRevokeLeaseRequest as DynamicSecretsRevokeLeaseRequestModel,
)
from ..models.DynamicSecretsRevokeLease200Response import (
    DynamicSecretsRevokeLease200Response as DynamicSecretsRevokeLease200ResponseModel,
)


class DynamicSecrets(BaseService):
    def issue_lease(self, request_input: DynamicSecretsIssueLeaseRequestModel = None):
        """
        Issue Lease
        """

        url_endpoint = "/v3/configs/config/dynamic_secrets/dynamic_secret/leases"
        headers = {"Content-type": "application/json"}
        self._add_required_headers(headers)

        final_url = self._url_prefix + url_endpoint
        res = self._http.post(final_url, headers, request_input, True)
        return res

    def revoke_lease(
        self, request_input: DynamicSecretsRevokeLeaseRequestModel = None
    ) -> DynamicSecretsRevokeLease200ResponseModel:
        """
        Revoke Lease
        """

        url_endpoint = "/v3/configs/config/dynamic_secrets/dynamic_secret/leases/lease"
        headers = {"Content-type": "application/json"}
        self._add_required_headers(headers)

        final_url = self._url_prefix + url_endpoint
        res = self._http.delete(final_url, headers, True)
        if res and isinstance(res, dict):
            return DynamicSecretsRevokeLease200ResponseModel(**res)
        return res

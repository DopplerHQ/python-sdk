import unittest
import responses
from src.dopplersdk.net.http_client import HTTPClient
from http_exceptions import ClientException
from src.dopplersdk.services.dynamic_secrets import DynamicSecrets


class TestDynamicSecrets_(unittest.TestCase):
    def test_true(self):
        self.assertTrue(True)

    @responses.activate
    def test_issue_lease(self):
        # Mock the API response
        responses.post(
            "https://api.doppler.com/v3/configs/config/dynamic_secrets/dynamic_secret/leases",
            json={},
            status=200,
        )
        # call the method to test
        test_service = DynamicSecrets("testkey")
        response = test_service.issue_lease({})
        self.assertEqual(response, {})
        responses.reset(),

    @responses.activate
    def test_issue_lease_error_on_non_200(self):
        # Mock the API response
        responses.post(
            "https://api.doppler.com/v3/configs/config/dynamic_secrets/dynamic_secret/leases",
            json={},
            status=404,
        )
        with self.assertRaises(ClientException):
            test_service = DynamicSecrets("testkey")
            test_service.issue_lease({})
        responses.reset()

    @responses.activate
    def test_revoke_lease(self):
        # Mock the API response
        responses.delete(
            "https://api.doppler.com/v3/configs/config/dynamic_secrets/dynamic_secret/leases/lease",
            json={},
            status=200,
        )
        # call the method to test
        test_service = DynamicSecrets("testkey")
        response = test_service.revoke_lease({})
        self.assertEqual(response, {})
        responses.reset(),

    @responses.activate
    def test_revoke_lease_error_on_non_200(self):
        # Mock the API response
        responses.delete(
            "https://api.doppler.com/v3/configs/config/dynamic_secrets/dynamic_secret/leases/lease",
            json={},
            status=404,
        )
        with self.assertRaises(ClientException):
            test_service = DynamicSecrets("testkey")
            test_service.revoke_lease({})
        responses.reset()


if __name__ == "__main__":
    unittest.main()

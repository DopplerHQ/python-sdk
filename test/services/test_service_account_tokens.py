import unittest
import responses
from src.dopplersdk.net.http_client import HTTPClient
from http_exceptions import ClientException
from src.dopplersdk.services.service_account_tokens import ServiceAccountTokens


class TestServiceAccountTokens_(unittest.TestCase):
    def test_true(self):
        self.assertTrue(True)

    @responses.activate
    def test_list(self):
        # Mock the API response
        responses.get(
            "https://api.doppler.com/v3/workplace/service_accounts/service_account/atque/tokens",
            json={},
            status=200,
        )
        # call the method to test
        test_service = ServiceAccountTokens("testkey")
        response = test_service.list("atque", 4, 6)
        self.assertEqual(response, {})
        responses.reset(),

    @responses.activate
    def test_list_required_fields_missing(self):
        # Mock the API response
        responses.get(
            "https://api.doppler.com/v3/workplace/service_accounts/service_account/accusamus/tokens",
            json={},
            status=202,
        )
        with self.assertRaises(TypeError):
            test_service = ServiceAccountTokens("testkey")
            test_service.list()
        responses.reset(),

    @responses.activate
    def test_list_error_on_non_200(self):
        # Mock the API response
        responses.get(
            "https://api.doppler.com/v3/workplace/service_accounts/service_account/itaque/tokens",
            json={},
            status=404,
        )
        with self.assertRaises(ClientException):
            test_service = ServiceAccountTokens("testkey")
            test_service.list("itaque", 8, 5)
        responses.reset()

    @responses.activate
    def test_create(self):
        # Mock the API response
        responses.post(
            "https://api.doppler.com/v3/workplace/service_accounts/service_account/quia/tokens",
            json={},
            status=200,
        )
        # call the method to test
        test_service = ServiceAccountTokens("testkey")
        response = test_service.create("quia", {})
        self.assertEqual(response, {})
        responses.reset(),

    @responses.activate
    def test_create_required_fields_missing(self):
        # Mock the API response
        responses.post(
            "https://api.doppler.com/v3/workplace/service_accounts/service_account/nostrum/tokens",
            json={},
            status=202,
        )
        with self.assertRaises(TypeError):
            test_service = ServiceAccountTokens("testkey")
            test_service.create()
        responses.reset(),

    @responses.activate
    def test_create_error_on_non_200(self):
        # Mock the API response
        responses.post(
            "https://api.doppler.com/v3/workplace/service_accounts/service_account/quas/tokens",
            json={},
            status=404,
        )
        with self.assertRaises(ClientException):
            test_service = ServiceAccountTokens("testkey")
            test_service.create("quas", {})
        responses.reset()

    @responses.activate
    def test_get(self):
        # Mock the API response
        responses.get(
            "https://api.doppler.com/v3/workplace/service_accounts/service_account/amet/tokens/token/eaque",
            json={},
            status=200,
        )
        # call the method to test
        test_service = ServiceAccountTokens("testkey")
        response = test_service.get("eaque", "amet")
        self.assertEqual(response, {})
        responses.reset(),

    @responses.activate
    def test_get_required_fields_missing(self):
        # Mock the API response
        responses.get(
            "https://api.doppler.com/v3/workplace/service_accounts/service_account/omnis/tokens/token/ullam",
            json={},
            status=202,
        )
        with self.assertRaises(TypeError):
            test_service = ServiceAccountTokens("testkey")
            test_service.get()
        responses.reset(),

    @responses.activate
    def test_get_error_on_non_200(self):
        # Mock the API response
        responses.get(
            "https://api.doppler.com/v3/workplace/service_accounts/service_account/perspiciatis/tokens/token/tempore",
            json={},
            status=404,
        )
        with self.assertRaises(ClientException):
            test_service = ServiceAccountTokens("testkey")
            test_service.get("tempore", "perspiciatis")
        responses.reset()

    @responses.activate
    def test_delete(self):
        # Mock the API response
        responses.delete(
            "https://api.doppler.com/v3/workplace/service_accounts/service_account/quos/tokens/token/praesentium",
            json={},
            status=200,
        )
        # call the method to test
        test_service = ServiceAccountTokens("testkey")
        response = test_service.delete("praesentium", "quos")
        self.assertEqual(response, {})
        responses.reset(),

    @responses.activate
    def test_delete_required_fields_missing(self):
        # Mock the API response
        responses.delete(
            "https://api.doppler.com/v3/workplace/service_accounts/service_account/id/tokens/token/expedita",
            json={},
            status=202,
        )
        with self.assertRaises(TypeError):
            test_service = ServiceAccountTokens("testkey")
            test_service.delete()
        responses.reset(),

    @responses.activate
    def test_delete_error_on_non_200(self):
        # Mock the API response
        responses.delete(
            "https://api.doppler.com/v3/workplace/service_accounts/service_account/minus/tokens/token/architecto",
            json={},
            status=404,
        )
        with self.assertRaises(ClientException):
            test_service = ServiceAccountTokens("testkey")
            test_service.delete("architecto", "minus")
        responses.reset()


if __name__ == "__main__":
    unittest.main()

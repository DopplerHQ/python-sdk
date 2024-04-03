import unittest
import responses
from src.dopplersdk.net.http_client import HTTPClient
from http_exceptions import ClientException
from src.dopplersdk.services.service_tokens import ServiceTokens


class TestServiceTokens_(unittest.TestCase):
    def test_true(self):
        self.assertTrue(True)

    @responses.activate
    def test_delete(self):
        # Mock the API response
        responses.delete(
            "https://api.doppler.com/v3/configs/config/tokens/token",
            json={},
            status=200,
        )
        # call the method to test
        test_service = ServiceTokens("testkey")
        response = test_service.delete({})
        self.assertEqual(response, {})
        responses.reset(),

    @responses.activate
    def test_delete_error_on_non_200(self):
        # Mock the API response
        responses.delete(
            "https://api.doppler.com/v3/configs/config/tokens/token",
            json={},
            status=404,
        )
        with self.assertRaises(ClientException):
            test_service = ServiceTokens("testkey")
            test_service.delete({})
        responses.reset()

    @responses.activate
    def test_list(self):
        # Mock the API response
        responses.get(
            "https://api.doppler.com/v3/configs/config/tokens", json={}, status=200
        )
        # call the method to test
        test_service = ServiceTokens("testkey")
        response = test_service.list("ea", "similique")
        self.assertEqual(response, {})
        responses.reset(),

    @responses.activate
    def test_list_required_fields_missing(self):
        # Mock the API response
        responses.get(
            "https://api.doppler.com/v3/configs/config/tokens", json={}, status=202
        )
        with self.assertRaises(TypeError):
            test_service = ServiceTokens("testkey")
            test_service.list()
        responses.reset(),

    @responses.activate
    def test_list_error_on_non_200(self):
        # Mock the API response
        responses.get(
            "https://api.doppler.com/v3/configs/config/tokens", json={}, status=404
        )
        with self.assertRaises(ClientException):
            test_service = ServiceTokens("testkey")
            test_service.list("impedit", "ipsam")
        responses.reset()

    @responses.activate
    def test_create(self):
        # Mock the API response
        responses.post(
            "https://api.doppler.com/v3/configs/config/tokens", json={}, status=200
        )
        # call the method to test
        test_service = ServiceTokens("testkey")
        response = test_service.create({})
        self.assertEqual(response, {})
        responses.reset(),

    @responses.activate
    def test_create_error_on_non_200(self):
        # Mock the API response
        responses.post(
            "https://api.doppler.com/v3/configs/config/tokens", json={}, status=404
        )
        with self.assertRaises(ClientException):
            test_service = ServiceTokens("testkey")
            test_service.create({})
        responses.reset()


if __name__ == "__main__":
    unittest.main()

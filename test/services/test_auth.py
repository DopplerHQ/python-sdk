import unittest
import responses
from src.dopplersdk.net.http_client import HTTPClient
from http_exceptions import ClientException
from src.dopplersdk.services.auth import Auth


class TestAuth_(unittest.TestCase):
    def test_true(self):
        self.assertTrue(True)

    @responses.activate
    def test_revoke(self):
        # Mock the API response
        responses.post("https://api.doppler.com/v3/auth/revoke", json={}, status=200)
        # call the method to test
        test_service = Auth("testkey")
        response = test_service.revoke({})
        self.assertEqual(response, {})
        responses.reset(),

    @responses.activate
    def test_revoke_error_on_non_200(self):
        # Mock the API response
        responses.post("https://api.doppler.com/v3/auth/revoke", json={}, status=404)
        with self.assertRaises(ClientException):
            test_service = Auth("testkey")
            test_service.revoke({})
        responses.reset()

    @responses.activate
    def test_me(self):
        # Mock the API response
        responses.get("https://api.doppler.com/v3/me", json={}, status=200)
        # call the method to test
        test_service = Auth("testkey")
        response = test_service.me()
        self.assertEqual(response, {})
        responses.reset(),

    @responses.activate
    def test_me_error_on_non_200(self):
        # Mock the API response
        responses.get("https://api.doppler.com/v3/me", json={}, status=404)
        with self.assertRaises(ClientException):
            test_service = Auth("testkey")
            test_service.me()
        responses.reset()


if __name__ == "__main__":
    unittest.main()

import unittest
import responses
from src.dopplersdk.net.http_client import HTTPClient
from http_exceptions import ClientException
from src.dopplersdk.services.workplace import Workplace


class TestWorkplace_(unittest.TestCase):
    def test_true(self):
        self.assertTrue(True)

    @responses.activate
    def test_get(self):
        # Mock the API response
        responses.get("https://api.doppler.com/v3/workplace", json={}, status=200)
        # call the method to test
        test_service = Workplace("testkey")
        response = test_service.get()
        self.assertEqual(response, {})
        responses.reset(),

    @responses.activate
    def test_get_error_on_non_200(self):
        # Mock the API response
        responses.get("https://api.doppler.com/v3/workplace", json={}, status=404)
        with self.assertRaises(ClientException):
            test_service = Workplace("testkey")
            test_service.get()
        responses.reset()

    @responses.activate
    def test_update(self):
        # Mock the API response
        responses.post("https://api.doppler.com/v3/workplace", json={}, status=200)
        # call the method to test
        test_service = Workplace("testkey")
        response = test_service.update({})
        self.assertEqual(response, {})
        responses.reset(),

    @responses.activate
    def test_update_error_on_non_200(self):
        # Mock the API response
        responses.post("https://api.doppler.com/v3/workplace", json={}, status=404)
        with self.assertRaises(ClientException):
            test_service = Workplace("testkey")
            test_service.update({})
        responses.reset()


if __name__ == "__main__":
    unittest.main()

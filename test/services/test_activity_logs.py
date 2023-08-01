import unittest
import responses
from src.dopplersdk.net.http_client import HTTPClient
from http_exceptions import ClientException
from src.dopplersdk.services.activity_logs import ActivityLogs


class TestActivityLogs_(unittest.TestCase):
    def test_true(self):
        self.assertTrue(True)

    @responses.activate
    def test_retrieve(self):
        # Mock the API response
        responses.get("https://api.doppler.com/v3/logs/log", json={}, status=200)
        # call the method to test
        test_service = ActivityLogs("testkey")
        response = test_service.retrieve("et")
        self.assertEqual(response, {})
        responses.reset(),

    @responses.activate
    def test_retrieve_required_fields_missing(self):
        # Mock the API response
        responses.get("https://api.doppler.com/v3/logs/log", json={}, status=202)
        with self.assertRaises(TypeError):
            test_service = ActivityLogs("testkey")
            test_service.retrieve()
        responses.reset(),

    @responses.activate
    def test_retrieve_error_on_non_200(self):
        # Mock the API response
        responses.get("https://api.doppler.com/v3/logs/log", json={}, status=404)
        with self.assertRaises(ClientException):
            test_service = ActivityLogs("testkey")
            test_service.retrieve("eveniet")
        responses.reset()

    @responses.activate
    def test_list(self):
        # Mock the API response
        responses.get("https://api.doppler.com/v3/logs", json={}, status=200)
        # call the method to test
        test_service = ActivityLogs("testkey")
        response = test_service.list("recusandae", 7)
        self.assertEqual(response, {})
        responses.reset(),

    @responses.activate
    def test_list_error_on_non_200(self):
        # Mock the API response
        responses.get("https://api.doppler.com/v3/logs", json={}, status=404)
        with self.assertRaises(ClientException):
            test_service = ActivityLogs("testkey")
            test_service.list("earum", 2)
        responses.reset()


if __name__ == "__main__":
    unittest.main()

import unittest
import responses
from src.dopplersdk.net.http_client import HTTPClient
from http_exceptions import ClientException
from src.dopplersdk.services.config_logs import ConfigLogs


class TestConfigLogs_(unittest.TestCase):
    def test_true(self):
        self.assertTrue(True)

    @responses.activate
    def test_list(self):
        # Mock the API response
        responses.get(
            "https://api.doppler.com/v3/configs/config/logs", json={}, status=200
        )
        # call the method to test
        test_service = ConfigLogs("testkey")
        response = test_service.list("dolorem", "voluptatum", 8, 4)
        self.assertEqual(response, {})
        responses.reset(),

    @responses.activate
    def test_list_required_fields_missing(self):
        # Mock the API response
        responses.get(
            "https://api.doppler.com/v3/configs/config/logs", json={}, status=202
        )
        with self.assertRaises(TypeError):
            test_service = ConfigLogs("testkey")
            test_service.list()
        responses.reset(),

    @responses.activate
    def test_list_error_on_non_200(self):
        # Mock the API response
        responses.get(
            "https://api.doppler.com/v3/configs/config/logs", json={}, status=404
        )
        with self.assertRaises(ClientException):
            test_service = ConfigLogs("testkey")
            test_service.list("enim", "exercitationem", 8, 9)
        responses.reset()

    @responses.activate
    def test_get(self):
        # Mock the API response
        responses.get(
            "https://api.doppler.com/v3/configs/config/logs/log", json={}, status=200
        )
        # call the method to test
        test_service = ConfigLogs("testkey")
        response = test_service.get("fuga", "amet", "odit")
        self.assertEqual(response, {})
        responses.reset(),

    @responses.activate
    def test_get_required_fields_missing(self):
        # Mock the API response
        responses.get(
            "https://api.doppler.com/v3/configs/config/logs/log", json={}, status=202
        )
        with self.assertRaises(TypeError):
            test_service = ConfigLogs("testkey")
            test_service.get()
        responses.reset(),

    @responses.activate
    def test_get_error_on_non_200(self):
        # Mock the API response
        responses.get(
            "https://api.doppler.com/v3/configs/config/logs/log", json={}, status=404
        )
        with self.assertRaises(ClientException):
            test_service = ConfigLogs("testkey")
            test_service.get("sunt", "repellendus", "explicabo")
        responses.reset()

    @responses.activate
    def test_rollback(self):
        # Mock the API response
        responses.post(
            "https://api.doppler.com/v3/configs/config/logs/log/rollback",
            json={},
            status=200,
        )
        # call the method to test
        test_service = ConfigLogs("testkey")
        response = test_service.rollback("unde", "laborum", "magnam")
        self.assertEqual(response, {})
        responses.reset(),

    @responses.activate
    def test_rollback_required_fields_missing(self):
        # Mock the API response
        responses.post(
            "https://api.doppler.com/v3/configs/config/logs/log/rollback",
            json={},
            status=202,
        )
        with self.assertRaises(TypeError):
            test_service = ConfigLogs("testkey")
            test_service.rollback()
        responses.reset(),

    @responses.activate
    def test_rollback_error_on_non_200(self):
        # Mock the API response
        responses.post(
            "https://api.doppler.com/v3/configs/config/logs/log/rollback",
            json={},
            status=404,
        )
        with self.assertRaises(ClientException):
            test_service = ConfigLogs("testkey")
            test_service.rollback("atque", "eveniet", "quas")
        responses.reset()


if __name__ == "__main__":
    unittest.main()

import unittest
import responses
from src.dopplersdk.net.http_client import HTTPClient
from http_exceptions import ClientException
from src.dopplersdk.services.trusted_ips import TrustedIps


class TestTrustedIps_(unittest.TestCase):
    def test_true(self):
        self.assertTrue(True)

    @responses.activate
    def test_list(self):
        # Mock the API response
        responses.get(
            "https://api.doppler.com/v3/configs/config/trusted_ips", json={}, status=200
        )
        # call the method to test
        test_service = TrustedIps("testkey")
        response = test_service.list("voluptates", "repellat")
        self.assertEqual(response, {})
        responses.reset(),

    @responses.activate
    def test_list_required_fields_missing(self):
        # Mock the API response
        responses.get(
            "https://api.doppler.com/v3/configs/config/trusted_ips", json={}, status=202
        )
        with self.assertRaises(TypeError):
            test_service = TrustedIps("testkey")
            test_service.list()
        responses.reset(),

    @responses.activate
    def test_list_error_on_non_200(self):
        # Mock the API response
        responses.get(
            "https://api.doppler.com/v3/configs/config/trusted_ips", json={}, status=404
        )
        with self.assertRaises(ClientException):
            test_service = TrustedIps("testkey")
            test_service.list("assumenda", "illo")
        responses.reset()

    @responses.activate
    def test_add(self):
        # Mock the API response
        responses.post(
            "https://api.doppler.com/v3/configs/config/trusted_ips", json={}, status=200
        )
        # call the method to test
        test_service = TrustedIps("testkey")
        response = test_service.add("deleniti", "earum", {})
        self.assertEqual(response, {})
        responses.reset(),

    @responses.activate
    def test_add_required_fields_missing(self):
        # Mock the API response
        responses.post(
            "https://api.doppler.com/v3/configs/config/trusted_ips", json={}, status=202
        )
        with self.assertRaises(TypeError):
            test_service = TrustedIps("testkey")
            test_service.add()
        responses.reset(),

    @responses.activate
    def test_add_error_on_non_200(self):
        # Mock the API response
        responses.post(
            "https://api.doppler.com/v3/configs/config/trusted_ips", json={}, status=404
        )
        with self.assertRaises(ClientException):
            test_service = TrustedIps("testkey")
            test_service.add("laudantium", "animi", {})
        responses.reset()

    @responses.activate
    def test_delete(self):
        # Mock the API response
        responses.delete(
            "https://api.doppler.com/v3/configs/config/trusted_ips", json={}, status=200
        )
        # call the method to test
        test_service = TrustedIps("testkey")
        response = test_service.delete("eum", "nisi", {})
        self.assertEqual(response, {})
        responses.reset(),

    @responses.activate
    def test_delete_required_fields_missing(self):
        # Mock the API response
        responses.delete(
            "https://api.doppler.com/v3/configs/config/trusted_ips", json={}, status=202
        )
        with self.assertRaises(TypeError):
            test_service = TrustedIps("testkey")
            test_service.delete()
        responses.reset(),

    @responses.activate
    def test_delete_error_on_non_200(self):
        # Mock the API response
        responses.delete(
            "https://api.doppler.com/v3/configs/config/trusted_ips", json={}, status=404
        )
        with self.assertRaises(ClientException):
            test_service = TrustedIps("testkey")
            test_service.delete("quibusdam", "assumenda", {})
        responses.reset()


if __name__ == "__main__":
    unittest.main()

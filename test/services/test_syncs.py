import unittest
import responses
from src.dopplersdk.net.http_client import HTTPClient
from http_exceptions import ClientException
from src.dopplersdk.services.syncs import Syncs


class TestSyncs_(unittest.TestCase):
    def test_true(self):
        self.assertTrue(True)

    @responses.activate
    def test_create(self):
        # Mock the API response
        responses.post(
            "https://api.doppler.com/v3/configs/config/syncs", json={}, status=200
        )
        # call the method to test
        test_service = Syncs("testkey")
        response = test_service.create("reprehenderit", "ipsa", {})
        self.assertEqual(response, {})
        responses.reset(),

    @responses.activate
    def test_create_required_fields_missing(self):
        # Mock the API response
        responses.post(
            "https://api.doppler.com/v3/configs/config/syncs", json={}, status=202
        )
        with self.assertRaises(TypeError):
            test_service = Syncs("testkey")
            test_service.create()
        responses.reset(),

    @responses.activate
    def test_create_error_on_non_200(self):
        # Mock the API response
        responses.post(
            "https://api.doppler.com/v3/configs/config/syncs", json={}, status=404
        )
        with self.assertRaises(ClientException):
            test_service = Syncs("testkey")
            test_service.create("eos", "repudiandae", {})
        responses.reset()

    @responses.activate
    def test_get(self):
        # Mock the API response
        responses.get(
            "https://api.doppler.com/v3/configs/config/syncs/sync", json={}, status=200
        )
        # call the method to test
        test_service = Syncs("testkey")
        response = test_service.get("minima", "quos", "ea")
        self.assertEqual(response, {})
        responses.reset(),

    @responses.activate
    def test_get_required_fields_missing(self):
        # Mock the API response
        responses.get(
            "https://api.doppler.com/v3/configs/config/syncs/sync", json={}, status=202
        )
        with self.assertRaises(TypeError):
            test_service = Syncs("testkey")
            test_service.get()
        responses.reset(),

    @responses.activate
    def test_get_error_on_non_200(self):
        # Mock the API response
        responses.get(
            "https://api.doppler.com/v3/configs/config/syncs/sync", json={}, status=404
        )
        with self.assertRaises(ClientException):
            test_service = Syncs("testkey")
            test_service.get("omnis", "sequi", "accusantium")
        responses.reset()

    @responses.activate
    def test_delete(self):
        # Mock the API response
        responses.delete(
            "https://api.doppler.com/v3/configs/config/syncs/sync", json={}, status=200
        )
        # call the method to test
        test_service = Syncs("testkey")
        response = test_service.delete(True, "natus", "molestiae", "ex")
        self.assertEqual(response, {})
        responses.reset(),

    @responses.activate
    def test_delete_required_fields_missing(self):
        # Mock the API response
        responses.delete(
            "https://api.doppler.com/v3/configs/config/syncs/sync", json={}, status=202
        )
        with self.assertRaises(TypeError):
            test_service = Syncs("testkey")
            test_service.delete()
        responses.reset(),

    @responses.activate
    def test_delete_error_on_non_200(self):
        # Mock the API response
        responses.delete(
            "https://api.doppler.com/v3/configs/config/syncs/sync", json={}, status=404
        )
        with self.assertRaises(ClientException):
            test_service = Syncs("testkey")
            test_service.delete(True, "sed", "laudantium", "dolor")
        responses.reset()


if __name__ == "__main__":
    unittest.main()

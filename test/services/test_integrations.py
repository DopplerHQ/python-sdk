import unittest
import responses
from src.dopplersdk.net.http_client import HTTPClient
from http_exceptions import ClientException
from src.dopplersdk.services.integrations import Integrations


class TestIntegrations_(unittest.TestCase):
    def test_true(self):
        self.assertTrue(True)

    @responses.activate
    def test_list(self):
        # Mock the API response
        responses.get("https://api.doppler.com/v3/integrations", json={}, status=200)
        # call the method to test
        test_service = Integrations("testkey")
        response = test_service.list()
        self.assertEqual(response, {})
        responses.reset(),

    @responses.activate
    def test_list_error_on_non_200(self):
        # Mock the API response
        responses.get("https://api.doppler.com/v3/integrations", json={}, status=404)
        with self.assertRaises(ClientException):
            test_service = Integrations("testkey")
            test_service.list()
        responses.reset()

    @responses.activate
    def test_create(self):
        # Mock the API response
        responses.post("https://api.doppler.com/v3/integrations", json={}, status=200)
        # call the method to test
        test_service = Integrations("testkey")
        response = test_service.create({})
        self.assertEqual(response, {})
        responses.reset(),

    @responses.activate
    def test_create_error_on_non_200(self):
        # Mock the API response
        responses.post("https://api.doppler.com/v3/integrations", json={}, status=404)
        with self.assertRaises(ClientException):
            test_service = Integrations("testkey")
            test_service.create({})
        responses.reset()

    @responses.activate
    def test_get(self):
        # Mock the API response
        responses.get(
            "https://api.doppler.com/v3/integrations/integration", json={}, status=200
        )
        # call the method to test
        test_service = Integrations("testkey")
        response = test_service.get("porro")
        self.assertEqual(response, {})
        responses.reset(),

    @responses.activate
    def test_get_required_fields_missing(self):
        # Mock the API response
        responses.get(
            "https://api.doppler.com/v3/integrations/integration", json={}, status=202
        )
        with self.assertRaises(TypeError):
            test_service = Integrations("testkey")
            test_service.get()
        responses.reset(),

    @responses.activate
    def test_get_error_on_non_200(self):
        # Mock the API response
        responses.get(
            "https://api.doppler.com/v3/integrations/integration", json={}, status=404
        )
        with self.assertRaises(ClientException):
            test_service = Integrations("testkey")
            test_service.get("magni")
        responses.reset()

    @responses.activate
    def test_update(self):
        # Mock the API response
        responses.put(
            "https://api.doppler.com/v3/integrations/integration", json={}, status=200
        )
        # call the method to test
        test_service = Integrations("testkey")
        response = test_service.update("numquam", {})
        self.assertEqual(response, {})
        responses.reset(),

    @responses.activate
    def test_update_required_fields_missing(self):
        # Mock the API response
        responses.put(
            "https://api.doppler.com/v3/integrations/integration", json={}, status=202
        )
        with self.assertRaises(TypeError):
            test_service = Integrations("testkey")
            test_service.update()
        responses.reset(),

    @responses.activate
    def test_update_error_on_non_200(self):
        # Mock the API response
        responses.put(
            "https://api.doppler.com/v3/integrations/integration", json={}, status=404
        )
        with self.assertRaises(ClientException):
            test_service = Integrations("testkey")
            test_service.update("facere", {})
        responses.reset()

    @responses.activate
    def test_delete(self):
        # Mock the API response
        responses.delete(
            "https://api.doppler.com/v3/integrations/integration", json={}, status=200
        )
        # call the method to test
        test_service = Integrations("testkey")
        response = test_service.delete("eligendi")
        self.assertEqual(response, {})
        responses.reset(),

    @responses.activate
    def test_delete_required_fields_missing(self):
        # Mock the API response
        responses.delete(
            "https://api.doppler.com/v3/integrations/integration", json={}, status=202
        )
        with self.assertRaises(TypeError):
            test_service = Integrations("testkey")
            test_service.delete()
        responses.reset(),

    @responses.activate
    def test_delete_error_on_non_200(self):
        # Mock the API response
        responses.delete(
            "https://api.doppler.com/v3/integrations/integration", json={}, status=404
        )
        with self.assertRaises(ClientException):
            test_service = Integrations("testkey")
            test_service.delete("unde")
        responses.reset()


if __name__ == "__main__":
    unittest.main()

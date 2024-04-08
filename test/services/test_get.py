import unittest
import responses
from src.dopplersdk.net.http_client import HTTPClient
from http_exceptions import ClientException
from src.dopplersdk.services.get import Get


class TestGet_(unittest.TestCase):
    def test_true(self):
        self.assertTrue(True)

    @responses.activate
    def test_options(self):
        # Mock the API response
        responses.get(
            "https://api.doppler.com/v3/integrations/integration/options",
            json={},
            status=200,
        )
        # call the method to test
        test_service = Get("testkey")
        response = test_service.options("atque")
        self.assertEqual(response, {})
        responses.reset(),

    @responses.activate
    def test_options_required_fields_missing(self):
        # Mock the API response
        responses.get(
            "https://api.doppler.com/v3/integrations/integration/options",
            json={},
            status=202,
        )
        with self.assertRaises(TypeError):
            test_service = Get("testkey")
            test_service.options()
        responses.reset(),

    @responses.activate
    def test_options_error_on_non_200(self):
        # Mock the API response
        responses.get(
            "https://api.doppler.com/v3/integrations/integration/options",
            json={},
            status=404,
        )
        with self.assertRaises(ClientException):
            test_service = Get("testkey")
            test_service.options("mollitia")
        responses.reset()


if __name__ == "__main__":
    unittest.main()

import unittest
import responses
from src.dopplersdk.net.http_client import HTTPClient
from http_exceptions import ClientException
from src.dopplersdk.services.users import Users


class TestUsers_(unittest.TestCase):
    def test_true(self):
        self.assertTrue(True)

    @responses.activate
    def test_list(self):
        # Mock the API response
        responses.get("https://api.doppler.com/v3/workplace/users", json={}, status=200)
        # call the method to test
        test_service = Users("testkey")
        response = test_service.list(4)
        self.assertEqual(response, {})
        responses.reset(),

    @responses.activate
    def test_list_error_on_non_200(self):
        # Mock the API response
        responses.get("https://api.doppler.com/v3/workplace/users", json={}, status=404)
        with self.assertRaises(ClientException):
            test_service = Users("testkey")
            test_service.list(7)
        responses.reset()

    @responses.activate
    def test_get(self):
        # Mock the API response
        responses.get(
            "https://api.doppler.com/v3/workplace/users/veniam", json={}, status=200
        )
        # call the method to test
        test_service = Users("testkey")
        response = test_service.get("veniam")
        self.assertEqual(response, {})
        responses.reset(),

    @responses.activate
    def test_get_required_fields_missing(self):
        # Mock the API response
        responses.get(
            "https://api.doppler.com/v3/workplace/users/sunt", json={}, status=202
        )
        with self.assertRaises(TypeError):
            test_service = Users("testkey")
            test_service.get()
        responses.reset(),

    @responses.activate
    def test_get_error_on_non_200(self):
        # Mock the API response
        responses.get(
            "https://api.doppler.com/v3/workplace/users/natus", json={}, status=404
        )
        with self.assertRaises(ClientException):
            test_service = Users("testkey")
            test_service.get("natus")
        responses.reset()


if __name__ == "__main__":
    unittest.main()

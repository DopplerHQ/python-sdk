import unittest
import responses
from src.dopplersdk.net.http_client import HTTPClient
from http_exceptions import ClientException
from src.dopplersdk.services.audit import Audit


class TestAudit_(unittest.TestCase):
    def test_true(self):
        self.assertTrue(True)

    @responses.activate
    def test_get_user(self):
        # Mock the API response
        responses.get(
            "https://api.doppler.com/v3/workplace/users/8242129968", json={}, status=200
        )
        # call the method to test
        test_service = Audit("testkey")
        response = test_service.get_user("8242129968", True)
        self.assertEqual(response, {})
        responses.reset(),

    @responses.activate
    def test_get_user_required_fields_missing(self):
        # Mock the API response
        responses.get(
            "https://api.doppler.com/v3/workplace/users/4946672611", json={}, status=202
        )
        with self.assertRaises(TypeError):
            test_service = Audit("testkey")
            test_service.get_user()
        responses.reset(),

    @responses.activate
    def test_get_user_error_on_non_200(self):
        # Mock the API response
        responses.get(
            "https://api.doppler.com/v3/workplace/users/8407007223", json={}, status=404
        )
        with self.assertRaises(ClientException):
            test_service = Audit("testkey")
            test_service.get_user("8407007223", True)
        responses.reset()


if __name__ == "__main__":
    unittest.main()

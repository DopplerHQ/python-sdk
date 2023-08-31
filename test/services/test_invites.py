import unittest
import responses
from src.dopplersdk.net.http_client import HTTPClient
from http_exceptions import ClientException
from src.dopplersdk.services.invites import Invites


class TestInvites_(unittest.TestCase):
    def test_true(self):
        self.assertTrue(True)

    @responses.activate
    def test_list(self):
        # Mock the API response
        responses.get(
            "https://api.doppler.com/v3/workplace/invites", json={}, status=200
        )
        # call the method to test
        test_service = Invites("testkey")
        response = test_service.list(3, 1)
        self.assertEqual(response, {})
        responses.reset(),

    @responses.activate
    def test_list_error_on_non_200(self):
        # Mock the API response
        responses.get(
            "https://api.doppler.com/v3/workplace/invites", json={}, status=404
        )
        with self.assertRaises(ClientException):
            test_service = Invites("testkey")
            test_service.list(7, 4)
        responses.reset()


if __name__ == "__main__":
    unittest.main()

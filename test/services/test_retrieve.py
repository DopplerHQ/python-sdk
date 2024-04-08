import unittest
import responses
from src.dopplersdk.net.http_client import HTTPClient
from http_exceptions import ClientException
from src.dopplersdk.services.retrieve import Retrieve


class TestRetrieve_(unittest.TestCase):
    def test_true(self):
        self.assertTrue(True)

    @responses.activate
    def test_member(self):
        # Mock the API response
        responses.get(
            "https://api.doppler.com/v3/workplace/groups/group/rerum/members/workplace_user/nam",
            json={},
            status=200,
        )
        # call the method to test
        test_service = Retrieve("testkey")
        response = test_service.member("nam", "workplace_user", "rerum")
        self.assertEqual(response, {})
        responses.reset(),

    @responses.activate
    def test_member_required_fields_missing(self):
        # Mock the API response
        responses.get(
            "https://api.doppler.com/v3/workplace/groups/group/eaque/members/workplace_user/rerum",
            json={},
            status=202,
        )
        with self.assertRaises(TypeError):
            test_service = Retrieve("testkey")
            test_service.member()
        responses.reset(),

    @responses.activate
    def test_member_error_on_non_200(self):
        # Mock the API response
        responses.get(
            "https://api.doppler.com/v3/workplace/groups/group/cum/members/workplace_user/eum",
            json={},
            status=404,
        )
        with self.assertRaises(ClientException):
            test_service = Retrieve("testkey")
            test_service.member("eum", "workplace_user", "cum")
        responses.reset()


if __name__ == "__main__":
    unittest.main()

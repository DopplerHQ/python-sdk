import unittest
import responses
from src.dopplersdk.net.http_client import HTTPClient
from http_exceptions import ClientException
from src.dopplersdk.services.project_members import ProjectMembers


class TestProjectMembers_(unittest.TestCase):
    def test_true(self):
        self.assertTrue(True)

    @responses.activate
    def test_list(self):
        # Mock the API response
        responses.get(
            "https://api.doppler.com/v3/projects/project/members", json={}, status=200
        )
        # call the method to test
        test_service = ProjectMembers("testkey")
        response = test_service.list("sed", 9, 2)
        self.assertEqual(response, {})
        responses.reset(),

    @responses.activate
    def test_list_required_fields_missing(self):
        # Mock the API response
        responses.get(
            "https://api.doppler.com/v3/projects/project/members", json={}, status=202
        )
        with self.assertRaises(TypeError):
            test_service = ProjectMembers("testkey")
            test_service.list()
        responses.reset(),

    @responses.activate
    def test_list_error_on_non_200(self):
        # Mock the API response
        responses.get(
            "https://api.doppler.com/v3/projects/project/members", json={}, status=404
        )
        with self.assertRaises(ClientException):
            test_service = ProjectMembers("testkey")
            test_service.list("placeat", 4, 4)
        responses.reset()

    @responses.activate
    def test_add(self):
        # Mock the API response
        responses.post(
            "https://api.doppler.com/v3/projects/project/members", json={}, status=200
        )
        # call the method to test
        test_service = ProjectMembers("testkey")
        response = test_service.add("impedit", {})
        self.assertEqual(response, {})
        responses.reset(),

    @responses.activate
    def test_add_required_fields_missing(self):
        # Mock the API response
        responses.post(
            "https://api.doppler.com/v3/projects/project/members", json={}, status=202
        )
        with self.assertRaises(TypeError):
            test_service = ProjectMembers("testkey")
            test_service.add()
        responses.reset(),

    @responses.activate
    def test_add_error_on_non_200(self):
        # Mock the API response
        responses.post(
            "https://api.doppler.com/v3/projects/project/members", json={}, status=404
        )
        with self.assertRaises(ClientException):
            test_service = ProjectMembers("testkey")
            test_service.add("nulla", {})
        responses.reset()

    @responses.activate
    def test_get(self):
        # Mock the API response
        responses.get(
            "https://api.doppler.com/v3/projects/project/members/member/workplace_user/minus",
            json={},
            status=200,
        )
        # call the method to test
        test_service = ProjectMembers("testkey")
        response = test_service.get("minus", "workplace_user", "molestiae")
        self.assertEqual(response, {})
        responses.reset(),

    @responses.activate
    def test_get_required_fields_missing(self):
        # Mock the API response
        responses.get(
            "https://api.doppler.com/v3/projects/project/members/member/workplace_user/cum",
            json={},
            status=202,
        )
        with self.assertRaises(TypeError):
            test_service = ProjectMembers("testkey")
            test_service.get()
        responses.reset(),

    @responses.activate
    def test_get_error_on_non_200(self):
        # Mock the API response
        responses.get(
            "https://api.doppler.com/v3/projects/project/members/member/workplace_user/molestiae",
            json={},
            status=404,
        )
        with self.assertRaises(ClientException):
            test_service = ProjectMembers("testkey")
            test_service.get("molestiae", "workplace_user", "expedita")
        responses.reset()

    @responses.activate
    def test_update(self):
        # Mock the API response
        responses.patch(
            "https://api.doppler.com/v3/projects/project/members/member/workplace_user/natus",
            json={},
            status=200,
        )
        # call the method to test
        test_service = ProjectMembers("testkey")
        response = test_service.update("dolore", "natus", "workplace_user", {})
        self.assertEqual(response, {})
        responses.reset(),

    @responses.activate
    def test_update_required_fields_missing(self):
        # Mock the API response
        responses.patch(
            "https://api.doppler.com/v3/projects/project/members/member/workplace_user/aperiam",
            json={},
            status=202,
        )
        with self.assertRaises(TypeError):
            test_service = ProjectMembers("testkey")
            test_service.update()
        responses.reset(),

    @responses.activate
    def test_update_error_on_non_200(self):
        # Mock the API response
        responses.patch(
            "https://api.doppler.com/v3/projects/project/members/member/workplace_user/dolores",
            json={},
            status=404,
        )
        with self.assertRaises(ClientException):
            test_service = ProjectMembers("testkey")
            test_service.update("modi", "dolores", "workplace_user", {})
        responses.reset()

    @responses.activate
    def test_delete(self):
        # Mock the API response
        responses.delete(
            "https://api.doppler.com/v3/projects/project/members/member/workplace_user/deserunt",
            json={},
            status=200,
        )
        # call the method to test
        test_service = ProjectMembers("testkey")
        response = test_service.delete("repellat", "deserunt", "workplace_user")
        self.assertEqual(response, {})
        responses.reset(),

    @responses.activate
    def test_delete_required_fields_missing(self):
        # Mock the API response
        responses.delete(
            "https://api.doppler.com/v3/projects/project/members/member/workplace_user/rem",
            json={},
            status=202,
        )
        with self.assertRaises(TypeError):
            test_service = ProjectMembers("testkey")
            test_service.delete()
        responses.reset(),

    @responses.activate
    def test_delete_error_on_non_200(self):
        # Mock the API response
        responses.delete(
            "https://api.doppler.com/v3/projects/project/members/member/workplace_user/ipsa",
            json={},
            status=404,
        )
        with self.assertRaises(ClientException):
            test_service = ProjectMembers("testkey")
            test_service.delete("perferendis", "ipsa", "workplace_user")
        responses.reset()


if __name__ == "__main__":
    unittest.main()

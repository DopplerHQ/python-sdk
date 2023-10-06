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
        response = test_service.list("aut", 6, 2)
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
            test_service.list("molestiae", 4, 5)
        responses.reset()

    @responses.activate
    def test_add(self):
        # Mock the API response
        responses.post(
            "https://api.doppler.com/v3/projects/project/members", json={}, status=200
        )
        # call the method to test
        test_service = ProjectMembers("testkey")
        response = test_service.add("beatae", {})
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
            test_service.add("aliquam", {})
        responses.reset()

    @responses.activate
    def test_get(self):
        # Mock the API response
        responses.get(
            "https://api.doppler.com/v3/projects/project/members/member/workplace_user/a",
            json={},
            status=200,
        )
        # call the method to test
        test_service = ProjectMembers("testkey")
        response = test_service.get("a", "workplace_user", "et")
        self.assertEqual(response, {})
        responses.reset(),

    @responses.activate
    def test_get_required_fields_missing(self):
        # Mock the API response
        responses.get(
            "https://api.doppler.com/v3/projects/project/members/member/workplace_user/aliquam",
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
            "https://api.doppler.com/v3/projects/project/members/member/workplace_user/magni",
            json={},
            status=404,
        )
        with self.assertRaises(ClientException):
            test_service = ProjectMembers("testkey")
            test_service.get("magni", "workplace_user", "saepe")
        responses.reset()

    @responses.activate
    def test_update(self):
        # Mock the API response
        responses.patch(
            "https://api.doppler.com/v3/projects/project/members/member/workplace_user/ipsum",
            json={},
            status=200,
        )
        # call the method to test
        test_service = ProjectMembers("testkey")
        response = test_service.update("recusandae", "ipsum", "workplace_user", {})
        self.assertEqual(response, {})
        responses.reset(),

    @responses.activate
    def test_update_required_fields_missing(self):
        # Mock the API response
        responses.patch(
            "https://api.doppler.com/v3/projects/project/members/member/workplace_user/sit",
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
            "https://api.doppler.com/v3/projects/project/members/member/workplace_user/reprehenderit",
            json={},
            status=404,
        )
        with self.assertRaises(ClientException):
            test_service = ProjectMembers("testkey")
            test_service.update("odit", "reprehenderit", "workplace_user", {})
        responses.reset()

    @responses.activate
    def test_delete(self):
        # Mock the API response
        responses.delete(
            "https://api.doppler.com/v3/projects/project/members/member/workplace_user/iure",
            json={},
            status=200,
        )
        # call the method to test
        test_service = ProjectMembers("testkey")
        response = test_service.delete("hic", "iure", "workplace_user")
        self.assertEqual(response, {})
        responses.reset(),

    @responses.activate
    def test_delete_required_fields_missing(self):
        # Mock the API response
        responses.delete(
            "https://api.doppler.com/v3/projects/project/members/member/workplace_user/provident",
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
            "https://api.doppler.com/v3/projects/project/members/member/workplace_user/sequi",
            json={},
            status=404,
        )
        with self.assertRaises(ClientException):
            test_service = ProjectMembers("testkey")
            test_service.delete("ab", "sequi", "workplace_user")
        responses.reset()


if __name__ == "__main__":
    unittest.main()

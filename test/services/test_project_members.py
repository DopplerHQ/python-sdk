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
        response = test_service.list("debitis", 2, 1)
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
            test_service.list("eos", 8, 2)
        responses.reset()

    @responses.activate
    def test_add(self):
        # Mock the API response
        responses.post(
            "https://api.doppler.com/v3/projects/project/members", json={}, status=200
        )
        # call the method to test
        test_service = ProjectMembers("testkey")
        response = test_service.add("excepturi", {})
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
            test_service.add("facilis", {})
        responses.reset()

    @responses.activate
    def test_get(self):
        # Mock the API response
        responses.get(
            "https://api.doppler.com/v3/projects/project/members/member/workplace_user/mollitia",
            json={},
            status=200,
        )
        # call the method to test
        test_service = ProjectMembers("testkey")
        response = test_service.get("mollitia", "workplace_user", "voluptates")
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
            "https://api.doppler.com/v3/projects/project/members/member/workplace_user/labore",
            json={},
            status=404,
        )
        with self.assertRaises(ClientException):
            test_service = ProjectMembers("testkey")
            test_service.get("labore", "workplace_user", "aliquam")
        responses.reset()

    @responses.activate
    def test_update(self):
        # Mock the API response
        responses.patch(
            "https://api.doppler.com/v3/projects/project/members/member/workplace_user/dolores",
            json={},
            status=200,
        )
        # call the method to test
        test_service = ProjectMembers("testkey")
        response = test_service.update("ullam", "dolores", "workplace_user", {})
        self.assertEqual(response, {})
        responses.reset(),

    @responses.activate
    def test_update_required_fields_missing(self):
        # Mock the API response
        responses.patch(
            "https://api.doppler.com/v3/projects/project/members/member/workplace_user/quasi",
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
            "https://api.doppler.com/v3/projects/project/members/member/workplace_user/quidem",
            json={},
            status=404,
        )
        with self.assertRaises(ClientException):
            test_service = ProjectMembers("testkey")
            test_service.update("adipisci", "quidem", "workplace_user", {})
        responses.reset()

    @responses.activate
    def test_delete(self):
        # Mock the API response
        responses.delete(
            "https://api.doppler.com/v3/projects/project/members/member/workplace_user/exercitationem",
            json={},
            status=200,
        )
        # call the method to test
        test_service = ProjectMembers("testkey")
        response = test_service.delete("occaecati", "exercitationem", "workplace_user")
        self.assertEqual(response, {})
        responses.reset(),

    @responses.activate
    def test_delete_required_fields_missing(self):
        # Mock the API response
        responses.delete(
            "https://api.doppler.com/v3/projects/project/members/member/workplace_user/iusto",
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
            "https://api.doppler.com/v3/projects/project/members/member/workplace_user/eos",
            json={},
            status=404,
        )
        with self.assertRaises(ClientException):
            test_service = ProjectMembers("testkey")
            test_service.delete("beatae", "eos", "workplace_user")
        responses.reset()


if __name__ == "__main__":
    unittest.main()

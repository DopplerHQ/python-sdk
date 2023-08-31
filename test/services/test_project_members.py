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
        response = test_service.list("asperiores", 9, 5)
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
            test_service.list("dolorem", 7, 3)
        responses.reset()

    @responses.activate
    def test_add(self):
        # Mock the API response
        responses.post(
            "https://api.doppler.com/v3/projects/project/members", json={}, status=200
        )
        # call the method to test
        test_service = ProjectMembers("testkey")
        response = test_service.add("blanditiis", {})
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
            test_service.add("magni", {})
        responses.reset()

    @responses.activate
    def test_get(self):
        # Mock the API response
        responses.get(
            "https://api.doppler.com/v3/projects/project/members/member/workplace_user/possimus",
            json={},
            status=200,
        )
        # call the method to test
        test_service = ProjectMembers("testkey")
        response = test_service.get("possimus", "workplace_user", "blanditiis")
        self.assertEqual(response, {})
        responses.reset(),

    @responses.activate
    def test_get_required_fields_missing(self):
        # Mock the API response
        responses.get(
            "https://api.doppler.com/v3/projects/project/members/member/workplace_user/praesentium",
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
            "https://api.doppler.com/v3/projects/project/members/member/workplace_user/earum",
            json={},
            status=404,
        )
        with self.assertRaises(ClientException):
            test_service = ProjectMembers("testkey")
            test_service.get("earum", "workplace_user", "iure")
        responses.reset()

    @responses.activate
    def test_update(self):
        # Mock the API response
        responses.patch(
            "https://api.doppler.com/v3/projects/project/members/member/workplace_user/enim",
            json={},
            status=200,
        )
        # call the method to test
        test_service = ProjectMembers("testkey")
        response = test_service.update("fugiat", "enim", "workplace_user", {})
        self.assertEqual(response, {})
        responses.reset(),

    @responses.activate
    def test_update_required_fields_missing(self):
        # Mock the API response
        responses.patch(
            "https://api.doppler.com/v3/projects/project/members/member/workplace_user/molestiae",
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
            "https://api.doppler.com/v3/projects/project/members/member/workplace_user/similique",
            json={},
            status=404,
        )
        with self.assertRaises(ClientException):
            test_service = ProjectMembers("testkey")
            test_service.update("veritatis", "similique", "workplace_user", {})
        responses.reset()

    @responses.activate
    def test_delete(self):
        # Mock the API response
        responses.delete(
            "https://api.doppler.com/v3/projects/project/members/member/workplace_user/mollitia",
            json={},
            status=200,
        )
        # call the method to test
        test_service = ProjectMembers("testkey")
        response = test_service.delete("autem", "mollitia", "workplace_user")
        self.assertEqual(response, {})
        responses.reset(),

    @responses.activate
    def test_delete_required_fields_missing(self):
        # Mock the API response
        responses.delete(
            "https://api.doppler.com/v3/projects/project/members/member/workplace_user/maiores",
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
            "https://api.doppler.com/v3/projects/project/members/member/workplace_user/doloribus",
            json={},
            status=404,
        )
        with self.assertRaises(ClientException):
            test_service = ProjectMembers("testkey")
            test_service.delete("accusantium", "doloribus", "workplace_user")
        responses.reset()


if __name__ == "__main__":
    unittest.main()

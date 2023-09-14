import unittest
import responses
from src.dopplersdk.net.http_client import HTTPClient
from http_exceptions import ClientException
from src.dopplersdk.services.project_roles import ProjectRoles


class TestProjectRoles_(unittest.TestCase):
    def test_true(self):
        self.assertTrue(True)

    @responses.activate
    def test_list(self):
        # Mock the API response
        responses.get("https://api.doppler.com/v3/projects/roles", json={}, status=200)
        # call the method to test
        test_service = ProjectRoles("testkey")
        response = test_service.list()
        self.assertEqual(response, {})
        responses.reset(),

    @responses.activate
    def test_list_error_on_non_200(self):
        # Mock the API response
        responses.get("https://api.doppler.com/v3/projects/roles", json={}, status=404)
        with self.assertRaises(ClientException):
            test_service = ProjectRoles("testkey")
            test_service.list()
        responses.reset()

    @responses.activate
    def test_create(self):
        # Mock the API response
        responses.post("https://api.doppler.com/v3/projects/roles", json={}, status=200)
        # call the method to test
        test_service = ProjectRoles("testkey")
        response = test_service.create()
        self.assertEqual(response, {})
        responses.reset(),

    @responses.activate
    def test_create_error_on_non_200(self):
        # Mock the API response
        responses.post("https://api.doppler.com/v3/projects/roles", json={}, status=404)
        with self.assertRaises(ClientException):
            test_service = ProjectRoles("testkey")
            test_service.create()
        responses.reset()

    @responses.activate
    def test_get(self):
        # Mock the API response
        responses.get(
            "https://api.doppler.com/v3/projects/roles/role/quia", json={}, status=200
        )
        # call the method to test
        test_service = ProjectRoles("testkey")
        response = test_service.get("quia")
        self.assertEqual(response, {})
        responses.reset(),

    @responses.activate
    def test_get_required_fields_missing(self):
        # Mock the API response
        responses.get(
            "https://api.doppler.com/v3/projects/roles/role/facere", json={}, status=202
        )
        with self.assertRaises(TypeError):
            test_service = ProjectRoles("testkey")
            test_service.get()
        responses.reset(),

    @responses.activate
    def test_get_error_on_non_200(self):
        # Mock the API response
        responses.get(
            "https://api.doppler.com/v3/projects/roles/role/sint", json={}, status=404
        )
        with self.assertRaises(ClientException):
            test_service = ProjectRoles("testkey")
            test_service.get("sint")
        responses.reset()

    @responses.activate
    def test_update(self):
        # Mock the API response
        responses.patch(
            "https://api.doppler.com/v3/projects/roles/role/ut", json={}, status=200
        )
        # call the method to test
        test_service = ProjectRoles("testkey")
        response = test_service.update("ut")
        self.assertEqual(response, {})
        responses.reset(),

    @responses.activate
    def test_update_required_fields_missing(self):
        # Mock the API response
        responses.patch(
            "https://api.doppler.com/v3/projects/roles/role/officia",
            json={},
            status=202,
        )
        with self.assertRaises(TypeError):
            test_service = ProjectRoles("testkey")
            test_service.update()
        responses.reset(),

    @responses.activate
    def test_update_error_on_non_200(self):
        # Mock the API response
        responses.patch(
            "https://api.doppler.com/v3/projects/roles/role/deleniti",
            json={},
            status=404,
        )
        with self.assertRaises(ClientException):
            test_service = ProjectRoles("testkey")
            test_service.update("deleniti")
        responses.reset()

    @responses.activate
    def test_delete(self):
        # Mock the API response
        responses.delete(
            "https://api.doppler.com/v3/projects/roles/role/a", json={}, status=200
        )
        # call the method to test
        test_service = ProjectRoles("testkey")
        response = test_service.delete("a")
        self.assertEqual(response, {})
        responses.reset(),

    @responses.activate
    def test_delete_required_fields_missing(self):
        # Mock the API response
        responses.delete(
            "https://api.doppler.com/v3/projects/roles/role/repellendus",
            json={},
            status=202,
        )
        with self.assertRaises(TypeError):
            test_service = ProjectRoles("testkey")
            test_service.delete()
        responses.reset(),

    @responses.activate
    def test_delete_error_on_non_200(self):
        # Mock the API response
        responses.delete(
            "https://api.doppler.com/v3/projects/roles/role/accusamus",
            json={},
            status=404,
        )
        with self.assertRaises(ClientException):
            test_service = ProjectRoles("testkey")
            test_service.delete("accusamus")
        responses.reset()

    @responses.activate
    def test_list_permissions(self):
        # Mock the API response
        responses.get(
            "https://api.doppler.com/v3/projects/permissions", json={}, status=200
        )
        # call the method to test
        test_service = ProjectRoles("testkey")
        response = test_service.list_permissions()
        self.assertEqual(response, {})
        responses.reset(),

    @responses.activate
    def test_list_permissions_error_on_non_200(self):
        # Mock the API response
        responses.get(
            "https://api.doppler.com/v3/projects/permissions", json={}, status=404
        )
        with self.assertRaises(ClientException):
            test_service = ProjectRoles("testkey")
            test_service.list_permissions()
        responses.reset()


if __name__ == "__main__":
    unittest.main()

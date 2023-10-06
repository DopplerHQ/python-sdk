import unittest
import responses
from src.dopplersdk.net.http_client import HTTPClient
from http_exceptions import ClientException
from src.dopplersdk.services.projects import Projects


class TestProjects_(unittest.TestCase):
    def test_true(self):
        self.assertTrue(True)

    @responses.activate
    def test_list(self):
        # Mock the API response
        responses.get("https://api.doppler.com/v3/projects", json={}, status=200)
        # call the method to test
        test_service = Projects("testkey")
        response = test_service.list(1, 4)
        self.assertEqual(response, {})
        responses.reset(),

    @responses.activate
    def test_list_error_on_non_200(self):
        # Mock the API response
        responses.get("https://api.doppler.com/v3/projects", json={}, status=404)
        with self.assertRaises(ClientException):
            test_service = Projects("testkey")
            test_service.list(7, 8)
        responses.reset()

    @responses.activate
    def test_create(self):
        # Mock the API response
        responses.post("https://api.doppler.com/v3/projects", json={}, status=200)
        # call the method to test
        test_service = Projects("testkey")
        response = test_service.create({})
        self.assertEqual(response, {})
        responses.reset(),

    @responses.activate
    def test_create_error_on_non_200(self):
        # Mock the API response
        responses.post("https://api.doppler.com/v3/projects", json={}, status=404)
        with self.assertRaises(ClientException):
            test_service = Projects("testkey")
            test_service.create({})
        responses.reset()

    @responses.activate
    def test_get(self):
        # Mock the API response
        responses.get(
            "https://api.doppler.com/v3/projects/project", json={}, status=200
        )
        # call the method to test
        test_service = Projects("testkey")
        response = test_service.get("maiores")
        self.assertEqual(response, {})
        responses.reset(),

    @responses.activate
    def test_get_required_fields_missing(self):
        # Mock the API response
        responses.get(
            "https://api.doppler.com/v3/projects/project", json={}, status=202
        )
        with self.assertRaises(TypeError):
            test_service = Projects("testkey")
            test_service.get()
        responses.reset(),

    @responses.activate
    def test_get_error_on_non_200(self):
        # Mock the API response
        responses.get(
            "https://api.doppler.com/v3/projects/project", json={}, status=404
        )
        with self.assertRaises(ClientException):
            test_service = Projects("testkey")
            test_service.get("ipsum")
        responses.reset()

    @responses.activate
    def test_update(self):
        # Mock the API response
        responses.post(
            "https://api.doppler.com/v3/projects/project", json={}, status=200
        )
        # call the method to test
        test_service = Projects("testkey")
        response = test_service.update({})
        self.assertEqual(response, {})
        responses.reset(),

    @responses.activate
    def test_update_error_on_non_200(self):
        # Mock the API response
        responses.post(
            "https://api.doppler.com/v3/projects/project", json={}, status=404
        )
        with self.assertRaises(ClientException):
            test_service = Projects("testkey")
            test_service.update({})
        responses.reset()

    @responses.activate
    def test_delete(self):
        # Mock the API response
        responses.delete(
            "https://api.doppler.com/v3/projects/project", json={}, status=200
        )
        # call the method to test
        test_service = Projects("testkey")
        response = test_service.delete({})
        self.assertEqual(response, {})
        responses.reset(),

    @responses.activate
    def test_delete_error_on_non_200(self):
        # Mock the API response
        responses.delete(
            "https://api.doppler.com/v3/projects/project", json={}, status=404
        )
        with self.assertRaises(ClientException):
            test_service = Projects("testkey")
            test_service.delete({})
        responses.reset()


if __name__ == "__main__":
    unittest.main()

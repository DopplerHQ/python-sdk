import unittest
import responses
from src.dopplersdk.net.http_client import HTTPClient
from http_exceptions import ClientException
from src.dopplersdk.services.configs import Configs


class TestConfigs_(unittest.TestCase):
    def test_true(self):
        self.assertTrue(True)

    @responses.activate
    def test_list(self):
        # Mock the API response
        responses.get("https://api.doppler.com/v3/configs", json={}, status=200)
        # call the method to test
        test_service = Configs("testkey")
        response = test_service.list("laboriosam", "suscipit", 8, 2)
        self.assertEqual(response, {})
        responses.reset(),

    @responses.activate
    def test_list_required_fields_missing(self):
        # Mock the API response
        responses.get("https://api.doppler.com/v3/configs", json={}, status=202)
        with self.assertRaises(TypeError):
            test_service = Configs("testkey")
            test_service.list()
        responses.reset(),

    @responses.activate
    def test_list_error_on_non_200(self):
        # Mock the API response
        responses.get("https://api.doppler.com/v3/configs", json={}, status=404)
        with self.assertRaises(ClientException):
            test_service = Configs("testkey")
            test_service.list("quo", "ipsum", 4, 9)
        responses.reset()

    @responses.activate
    def test_create(self):
        # Mock the API response
        responses.post("https://api.doppler.com/v3/configs", json={}, status=200)
        # call the method to test
        test_service = Configs("testkey")
        response = test_service.create({})
        self.assertEqual(response, {})
        responses.reset(),

    @responses.activate
    def test_create_error_on_non_200(self):
        # Mock the API response
        responses.post("https://api.doppler.com/v3/configs", json={}, status=404)
        with self.assertRaises(ClientException):
            test_service = Configs("testkey")
            test_service.create({})
        responses.reset()

    @responses.activate
    def test_get(self):
        # Mock the API response
        responses.get("https://api.doppler.com/v3/configs/config", json={}, status=200)
        # call the method to test
        test_service = Configs("testkey")
        response = test_service.get("numquam", "ducimus")
        self.assertEqual(response, {})
        responses.reset(),

    @responses.activate
    def test_get_required_fields_missing(self):
        # Mock the API response
        responses.get("https://api.doppler.com/v3/configs/config", json={}, status=202)
        with self.assertRaises(TypeError):
            test_service = Configs("testkey")
            test_service.get()
        responses.reset(),

    @responses.activate
    def test_get_error_on_non_200(self):
        # Mock the API response
        responses.get("https://api.doppler.com/v3/configs/config", json={}, status=404)
        with self.assertRaises(ClientException):
            test_service = Configs("testkey")
            test_service.get("voluptate", "maiores")
        responses.reset()

    @responses.activate
    def test_update(self):
        # Mock the API response
        responses.post("https://api.doppler.com/v3/configs/config", json={}, status=200)
        # call the method to test
        test_service = Configs("testkey")
        response = test_service.update({})
        self.assertEqual(response, {})
        responses.reset(),

    @responses.activate
    def test_update_error_on_non_200(self):
        # Mock the API response
        responses.post("https://api.doppler.com/v3/configs/config", json={}, status=404)
        with self.assertRaises(ClientException):
            test_service = Configs("testkey")
            test_service.update({})
        responses.reset()

    @responses.activate
    def test_delete(self):
        # Mock the API response
        responses.delete(
            "https://api.doppler.com/v3/configs/config", json={}, status=200
        )
        # call the method to test
        test_service = Configs("testkey")
        response = test_service.delete({})
        self.assertEqual(response, {})
        responses.reset(),

    @responses.activate
    def test_delete_error_on_non_200(self):
        # Mock the API response
        responses.delete(
            "https://api.doppler.com/v3/configs/config", json={}, status=404
        )
        with self.assertRaises(ClientException):
            test_service = Configs("testkey")
            test_service.delete({})
        responses.reset()

    @responses.activate
    def test_clone(self):
        # Mock the API response
        responses.post(
            "https://api.doppler.com/v3/configs/config/clone", json={}, status=200
        )
        # call the method to test
        test_service = Configs("testkey")
        response = test_service.clone({})
        self.assertEqual(response, {})
        responses.reset(),

    @responses.activate
    def test_clone_error_on_non_200(self):
        # Mock the API response
        responses.post(
            "https://api.doppler.com/v3/configs/config/clone", json={}, status=404
        )
        with self.assertRaises(ClientException):
            test_service = Configs("testkey")
            test_service.clone({})
        responses.reset()

    @responses.activate
    def test_lock(self):
        # Mock the API response
        responses.post(
            "https://api.doppler.com/v3/configs/config/lock", json={}, status=200
        )
        # call the method to test
        test_service = Configs("testkey")
        response = test_service.lock({})
        self.assertEqual(response, {})
        responses.reset(),

    @responses.activate
    def test_lock_error_on_non_200(self):
        # Mock the API response
        responses.post(
            "https://api.doppler.com/v3/configs/config/lock", json={}, status=404
        )
        with self.assertRaises(ClientException):
            test_service = Configs("testkey")
            test_service.lock({})
        responses.reset()

    @responses.activate
    def test_unlock(self):
        # Mock the API response
        responses.post(
            "https://api.doppler.com/v3/configs/config/unlock", json={}, status=200
        )
        # call the method to test
        test_service = Configs("testkey")
        response = test_service.unlock({})
        self.assertEqual(response, {})
        responses.reset(),

    @responses.activate
    def test_unlock_error_on_non_200(self):
        # Mock the API response
        responses.post(
            "https://api.doppler.com/v3/configs/config/unlock", json={}, status=404
        )
        with self.assertRaises(ClientException):
            test_service = Configs("testkey")
            test_service.unlock({})
        responses.reset()


if __name__ == "__main__":
    unittest.main()

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
        response = test_service.list("perspiciatis", "excepturi", 8, 4)
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
            test_service.list("nisi", "suscipit", 9, 4)
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
        response = test_service.get("at", "dolor")
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
            test_service.get("tempore", "officiis")
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

    @responses.activate
    def test_list_trusted_ips(self):
        # Mock the API response
        responses.get(
            "https://api.doppler.com/v3/configs/config/trusted_ips", json={}, status=200
        )
        # call the method to test
        test_service = Configs("testkey")
        response = test_service.list_trusted_ips("explicabo", "odio")
        self.assertEqual(response, {})
        responses.reset(),

    @responses.activate
    def test_list_trusted_ips_required_fields_missing(self):
        # Mock the API response
        responses.get(
            "https://api.doppler.com/v3/configs/config/trusted_ips", json={}, status=202
        )
        with self.assertRaises(TypeError):
            test_service = Configs("testkey")
            test_service.list_trusted_ips()
        responses.reset(),

    @responses.activate
    def test_list_trusted_ips_error_on_non_200(self):
        # Mock the API response
        responses.get(
            "https://api.doppler.com/v3/configs/config/trusted_ips", json={}, status=404
        )
        with self.assertRaises(ClientException):
            test_service = Configs("testkey")
            test_service.list_trusted_ips("optio", "adipisci")
        responses.reset()

    @responses.activate
    def test_add_trusted_ip(self):
        # Mock the API response
        responses.post(
            "https://api.doppler.com/v3/configs/config/trusted_ips", json={}, status=200
        )
        # call the method to test
        test_service = Configs("testkey")
        response = test_service.add_trusted_ip("laboriosam", "facere", {})
        self.assertEqual(response, {})
        responses.reset(),

    @responses.activate
    def test_add_trusted_ip_required_fields_missing(self):
        # Mock the API response
        responses.post(
            "https://api.doppler.com/v3/configs/config/trusted_ips", json={}, status=202
        )
        with self.assertRaises(TypeError):
            test_service = Configs("testkey")
            test_service.add_trusted_ip()
        responses.reset(),

    @responses.activate
    def test_add_trusted_ip_error_on_non_200(self):
        # Mock the API response
        responses.post(
            "https://api.doppler.com/v3/configs/config/trusted_ips", json={}, status=404
        )
        with self.assertRaises(ClientException):
            test_service = Configs("testkey")
            test_service.add_trusted_ip("excepturi", "adipisci", {})
        responses.reset()

    @responses.activate
    def test_delete_trusted_ip(self):
        # Mock the API response
        responses.delete(
            "https://api.doppler.com/v3/configs/config/trusted_ips", json={}, status=200
        )
        # call the method to test
        test_service = Configs("testkey")
        response = test_service.delete_trusted_ip("corrupti", "provident", {})
        self.assertEqual(response, {})
        responses.reset(),

    @responses.activate
    def test_delete_trusted_ip_required_fields_missing(self):
        # Mock the API response
        responses.delete(
            "https://api.doppler.com/v3/configs/config/trusted_ips", json={}, status=202
        )
        with self.assertRaises(TypeError):
            test_service = Configs("testkey")
            test_service.delete_trusted_ip()
        responses.reset(),

    @responses.activate
    def test_delete_trusted_ip_error_on_non_200(self):
        # Mock the API response
        responses.delete(
            "https://api.doppler.com/v3/configs/config/trusted_ips", json={}, status=404
        )
        with self.assertRaises(ClientException):
            test_service = Configs("testkey")
            test_service.delete_trusted_ip("magnam", "ab", {})
        responses.reset()


if __name__ == "__main__":
    unittest.main()

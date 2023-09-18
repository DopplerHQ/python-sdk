import unittest
import responses
from src.dopplersdk.net.http_client import HTTPClient
from http_exceptions import ClientException
from src.dopplersdk.services.secrets import Secrets


class TestSecrets_(unittest.TestCase):
    def test_true(self):
        self.assertTrue(True)

    @responses.activate
    def test_list(self):
        # Mock the API response
        responses.get(
            "https://api.doppler.com/v3/configs/config/secrets", json={}, status=200
        )
        # call the method to test
        test_service = Secrets("testkey")
        response = test_service.list(
            "cumque", "temporibus", "dolores", True, 8, "cum", True
        )
        self.assertEqual(response, {})
        responses.reset(),

    @responses.activate
    def test_list_required_fields_missing(self):
        # Mock the API response
        responses.get(
            "https://api.doppler.com/v3/configs/config/secrets", json={}, status=202
        )
        with self.assertRaises(TypeError):
            test_service = Secrets("testkey")
            test_service.list()
        responses.reset(),

    @responses.activate
    def test_list_error_on_non_200(self):
        # Mock the API response
        responses.get(
            "https://api.doppler.com/v3/configs/config/secrets", json={}, status=404
        )
        with self.assertRaises(ClientException):
            test_service = Secrets("testkey")
            test_service.list("fuga", "magnam", "similique", True, 4, "fugit", True)
        responses.reset()

    @responses.activate
    def test_update(self):
        # Mock the API response
        responses.post(
            "https://api.doppler.com/v3/configs/config/secrets", json={}, status=200
        )
        # call the method to test
        test_service = Secrets("testkey")
        response = test_service.update({})
        self.assertEqual(response, {})
        responses.reset(),

    @responses.activate
    def test_update_error_on_non_200(self):
        # Mock the API response
        responses.post(
            "https://api.doppler.com/v3/configs/config/secrets", json={}, status=404
        )
        with self.assertRaises(ClientException):
            test_service = Secrets("testkey")
            test_service.update({})
        responses.reset()

    @responses.activate
    def test_get(self):
        # Mock the API response
        responses.get(
            "https://api.doppler.com/v3/configs/config/secret", json={}, status=200
        )
        # call the method to test
        test_service = Secrets("testkey")
        response = test_service.get("Bonnie", "libero", "odio")
        self.assertEqual(response, {})
        responses.reset(),

    @responses.activate
    def test_get_required_fields_missing(self):
        # Mock the API response
        responses.get(
            "https://api.doppler.com/v3/configs/config/secret", json={}, status=202
        )
        with self.assertRaises(TypeError):
            test_service = Secrets("testkey")
            test_service.get()
        responses.reset(),

    @responses.activate
    def test_get_error_on_non_200(self):
        # Mock the API response
        responses.get(
            "https://api.doppler.com/v3/configs/config/secret", json={}, status=404
        )
        with self.assertRaises(ClientException):
            test_service = Secrets("testkey")
            test_service.get("Desiree", "quibusdam", "exercitationem")
        responses.reset()

    @responses.activate
    def test_delete(self):
        # Mock the API response
        responses.delete(
            "https://api.doppler.com/v3/configs/config/secret", json={}, status=200
        )
        # call the method to test
        test_service = Secrets("testkey")
        response = test_service.delete("Maci", "eos", "beatae")
        self.assertEqual(response, {})
        responses.reset(),

    @responses.activate
    def test_delete_required_fields_missing(self):
        # Mock the API response
        responses.delete(
            "https://api.doppler.com/v3/configs/config/secret", json={}, status=202
        )
        with self.assertRaises(TypeError):
            test_service = Secrets("testkey")
            test_service.delete()
        responses.reset(),

    @responses.activate
    def test_delete_error_on_non_200(self):
        # Mock the API response
        responses.delete(
            "https://api.doppler.com/v3/configs/config/secret", json={}, status=404
        )
        with self.assertRaises(ClientException):
            test_service = Secrets("testkey")
            test_service.delete("Domenic", "nisi", "iusto")
        responses.reset()

    @responses.activate
    def test_download(self):
        # Mock the API response
        responses.get(
            "https://api.doppler.com/v3/configs/config/secrets/download",
            json={},
            status=200,
        )
        # call the method to test
        test_service = Secrets("testkey")
        response = test_service.download(
            "necessitatibus", "suscipit", "json", "camel", True, 4
        )
        self.assertEqual(response, {})
        responses.reset(),

    @responses.activate
    def test_download_required_fields_missing(self):
        # Mock the API response
        responses.get(
            "https://api.doppler.com/v3/configs/config/secrets/download",
            json={},
            status=202,
        )
        with self.assertRaises(TypeError):
            test_service = Secrets("testkey")
            test_service.download()
        responses.reset(),

    @responses.activate
    def test_download_error_on_non_200(self):
        # Mock the API response
        responses.get(
            "https://api.doppler.com/v3/configs/config/secrets/download",
            json={},
            status=404,
        )
        with self.assertRaises(ClientException):
            test_service = Secrets("testkey")
            test_service.download("modi", "error", "json", "camel", True, 7)
        responses.reset()

    @responses.activate
    def test_names(self):
        # Mock the API response
        responses.get(
            "https://api.doppler.com/v3/configs/config/secrets/names",
            json={},
            status=200,
        )
        # call the method to test
        test_service = Secrets("testkey")
        response = test_service.names("facere", "autem", True, True)
        self.assertEqual(response, {})
        responses.reset(),

    @responses.activate
    def test_names_required_fields_missing(self):
        # Mock the API response
        responses.get(
            "https://api.doppler.com/v3/configs/config/secrets/names",
            json={},
            status=202,
        )
        with self.assertRaises(TypeError):
            test_service = Secrets("testkey")
            test_service.names()
        responses.reset(),

    @responses.activate
    def test_names_error_on_non_200(self):
        # Mock the API response
        responses.get(
            "https://api.doppler.com/v3/configs/config/secrets/names",
            json={},
            status=404,
        )
        with self.assertRaises(ClientException):
            test_service = Secrets("testkey")
            test_service.names("quis", "reiciendis", True, True)
        responses.reset()

    @responses.activate
    def test_update_note(self):
        # Mock the API response
        responses.post(
            "https://api.doppler.com/v3/configs/config/secrets/note",
            json={},
            status=200,
        )
        # call the method to test
        test_service = Secrets("testkey")
        response = test_service.update_note({})
        self.assertEqual(response, {})
        responses.reset(),

    @responses.activate
    def test_update_note_error_on_non_200(self):
        # Mock the API response
        responses.post(
            "https://api.doppler.com/v3/configs/config/secrets/note",
            json={},
            status=404,
        )
        with self.assertRaises(ClientException):
            test_service = Secrets("testkey")
            test_service.update_note({})
        responses.reset()


if __name__ == "__main__":
    unittest.main()

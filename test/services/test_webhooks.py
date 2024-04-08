import unittest
import responses
from src.dopplersdk.net.http_client import HTTPClient
from http_exceptions import ClientException
from src.dopplersdk.services.webhooks import Webhooks


class TestWebhooks_(unittest.TestCase):
    def test_true(self):
        self.assertTrue(True)

    @responses.activate
    def test_list(self):
        # Mock the API response
        responses.get("https://api.doppler.com/v3/webhooks", json={}, status=200)
        # call the method to test
        test_service = Webhooks("testkey")
        response = test_service.list("exercitationem")
        self.assertEqual(response, {})
        responses.reset(),

    @responses.activate
    def test_list_error_on_non_200(self):
        # Mock the API response
        responses.get("https://api.doppler.com/v3/webhooks", json={}, status=404)
        with self.assertRaises(ClientException):
            test_service = Webhooks("testkey")
            test_service.list("vel")
        responses.reset()

    @responses.activate
    def test_add(self):
        # Mock the API response
        responses.post("https://api.doppler.com/v3/webhooks", json={}, status=200)
        # call the method to test
        test_service = Webhooks("testkey")
        response = test_service.add("perspiciatis", {})
        self.assertEqual(response, {})
        responses.reset(),

    @responses.activate
    def test_add_error_on_non_200(self):
        # Mock the API response
        responses.post("https://api.doppler.com/v3/webhooks", json={}, status=404)
        with self.assertRaises(ClientException):
            test_service = Webhooks("testkey")
            test_service.add("error", {})
        responses.reset()

    @responses.activate
    def test_get(self):
        # Mock the API response
        responses.get(
            "https://api.doppler.com/v3/webhooks/webhook/enim", json={}, status=200
        )
        # call the method to test
        test_service = Webhooks("testkey")
        response = test_service.get("enim", "temporibus")
        self.assertEqual(response, {})
        responses.reset(),

    @responses.activate
    def test_get_required_fields_missing(self):
        # Mock the API response
        responses.get(
            "https://api.doppler.com/v3/webhooks/webhook/dolorem", json={}, status=202
        )
        with self.assertRaises(TypeError):
            test_service = Webhooks("testkey")
            test_service.get()
        responses.reset(),

    @responses.activate
    def test_get_error_on_non_200(self):
        # Mock the API response
        responses.get(
            "https://api.doppler.com/v3/webhooks/webhook/iusto", json={}, status=404
        )
        with self.assertRaises(ClientException):
            test_service = Webhooks("testkey")
            test_service.get("iusto", "sint")
        responses.reset()

    @responses.activate
    def test_update(self):
        # Mock the API response
        responses.patch(
            "https://api.doppler.com/v3/webhooks/webhook/maiores", json={}, status=200
        )
        # call the method to test
        test_service = Webhooks("testkey")
        response = test_service.update("maiores", "consequatur", {})
        self.assertEqual(response, {})
        responses.reset(),

    @responses.activate
    def test_update_required_fields_missing(self):
        # Mock the API response
        responses.patch(
            "https://api.doppler.com/v3/webhooks/webhook/provident", json={}, status=202
        )
        with self.assertRaises(TypeError):
            test_service = Webhooks("testkey")
            test_service.update()
        responses.reset(),

    @responses.activate
    def test_update_error_on_non_200(self):
        # Mock the API response
        responses.patch(
            "https://api.doppler.com/v3/webhooks/webhook/minus", json={}, status=404
        )
        with self.assertRaises(ClientException):
            test_service = Webhooks("testkey")
            test_service.update("minus", "ab", {})
        responses.reset()

    @responses.activate
    def test_delete(self):
        # Mock the API response
        responses.delete(
            "https://api.doppler.com/v3/webhooks/webhook/amet", json={}, status=200
        )
        # call the method to test
        test_service = Webhooks("testkey")
        response = test_service.delete("amet", "vitae")
        self.assertEqual(response, {})
        responses.reset(),

    @responses.activate
    def test_delete_required_fields_missing(self):
        # Mock the API response
        responses.delete(
            "https://api.doppler.com/v3/webhooks/webhook/placeat", json={}, status=202
        )
        with self.assertRaises(TypeError):
            test_service = Webhooks("testkey")
            test_service.delete()
        responses.reset(),

    @responses.activate
    def test_delete_error_on_non_200(self):
        # Mock the API response
        responses.delete(
            "https://api.doppler.com/v3/webhooks/webhook/unde", json={}, status=404
        )
        with self.assertRaises(ClientException):
            test_service = Webhooks("testkey")
            test_service.delete("unde", "deserunt")
        responses.reset()

    @responses.activate
    def test_enable(self):
        # Mock the API response
        responses.post(
            "https://api.doppler.com/v3/webhooks/webhook/in/enable", json={}, status=200
        )
        # call the method to test
        test_service = Webhooks("testkey")
        response = test_service.enable("in", "ad")
        self.assertEqual(response, {})
        responses.reset(),

    @responses.activate
    def test_enable_required_fields_missing(self):
        # Mock the API response
        responses.post(
            "https://api.doppler.com/v3/webhooks/webhook/eaque/enable",
            json={},
            status=202,
        )
        with self.assertRaises(TypeError):
            test_service = Webhooks("testkey")
            test_service.enable()
        responses.reset(),

    @responses.activate
    def test_enable_error_on_non_200(self):
        # Mock the API response
        responses.post(
            "https://api.doppler.com/v3/webhooks/webhook/animi/enable",
            json={},
            status=404,
        )
        with self.assertRaises(ClientException):
            test_service = Webhooks("testkey")
            test_service.enable("animi", "soluta")
        responses.reset()

    @responses.activate
    def test_disable(self):
        # Mock the API response
        responses.post(
            "https://api.doppler.com/v3/webhooks/webhook/porro/disable",
            json={},
            status=200,
        )
        # call the method to test
        test_service = Webhooks("testkey")
        response = test_service.disable("porro", "quis")
        self.assertEqual(response, {})
        responses.reset(),

    @responses.activate
    def test_disable_required_fields_missing(self):
        # Mock the API response
        responses.post(
            "https://api.doppler.com/v3/webhooks/webhook/cumque/disable",
            json={},
            status=202,
        )
        with self.assertRaises(TypeError):
            test_service = Webhooks("testkey")
            test_service.disable()
        responses.reset(),

    @responses.activate
    def test_disable_error_on_non_200(self):
        # Mock the API response
        responses.post(
            "https://api.doppler.com/v3/webhooks/webhook/veniam/disable",
            json={},
            status=404,
        )
        with self.assertRaises(ClientException):
            test_service = Webhooks("testkey")
            test_service.disable("veniam", "consequuntur")
        responses.reset()


if __name__ == "__main__":
    unittest.main()

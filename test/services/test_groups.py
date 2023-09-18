import unittest
import responses
from src.dopplersdk.net.http_client import HTTPClient
from http_exceptions import ClientException
from src.dopplersdk.services.groups import Groups


class TestGroups_(unittest.TestCase):
    def test_true(self):
        self.assertTrue(True)

    @responses.activate
    def test_list(self):
        # Mock the API response
        responses.get(
            "https://api.doppler.com/v3/workplace/groups", json={}, status=200
        )
        # call the method to test
        test_service = Groups("testkey")
        response = test_service.list(7, 2)
        self.assertEqual(response, {})
        responses.reset(),

    @responses.activate
    def test_list_error_on_non_200(self):
        # Mock the API response
        responses.get(
            "https://api.doppler.com/v3/workplace/groups", json={}, status=404
        )
        with self.assertRaises(ClientException):
            test_service = Groups("testkey")
            test_service.list(5, 8)
        responses.reset()

    @responses.activate
    def test_create(self):
        # Mock the API response
        responses.post(
            "https://api.doppler.com/v3/workplace/groups", json={}, status=200
        )
        # call the method to test
        test_service = Groups("testkey")
        response = test_service.create({})
        self.assertEqual(response, {})
        responses.reset(),

    @responses.activate
    def test_create_error_on_non_200(self):
        # Mock the API response
        responses.post(
            "https://api.doppler.com/v3/workplace/groups", json={}, status=404
        )
        with self.assertRaises(ClientException):
            test_service = Groups("testkey")
            test_service.create({})
        responses.reset()

    @responses.activate
    def test_get(self):
        # Mock the API response
        responses.get(
            "https://api.doppler.com/v3/workplace/groups/group/iusto",
            json={},
            status=200,
        )
        # call the method to test
        test_service = Groups("testkey")
        response = test_service.get("iusto")
        self.assertEqual(response, {})
        responses.reset(),

    @responses.activate
    def test_get_required_fields_missing(self):
        # Mock the API response
        responses.get(
            "https://api.doppler.com/v3/workplace/groups/group/suscipit",
            json={},
            status=202,
        )
        with self.assertRaises(TypeError):
            test_service = Groups("testkey")
            test_service.get()
        responses.reset(),

    @responses.activate
    def test_get_error_on_non_200(self):
        # Mock the API response
        responses.get(
            "https://api.doppler.com/v3/workplace/groups/group/omnis",
            json={},
            status=404,
        )
        with self.assertRaises(ClientException):
            test_service = Groups("testkey")
            test_service.get("omnis")
        responses.reset()

    @responses.activate
    def test_update(self):
        # Mock the API response
        responses.patch(
            "https://api.doppler.com/v3/workplace/groups/group/maxime",
            json={},
            status=200,
        )
        # call the method to test
        test_service = Groups("testkey")
        response = test_service.update("maxime", {})
        self.assertEqual(response, {})
        responses.reset(),

    @responses.activate
    def test_update_required_fields_missing(self):
        # Mock the API response
        responses.patch(
            "https://api.doppler.com/v3/workplace/groups/group/nisi",
            json={},
            status=202,
        )
        with self.assertRaises(TypeError):
            test_service = Groups("testkey")
            test_service.update()
        responses.reset(),

    @responses.activate
    def test_update_error_on_non_200(self):
        # Mock the API response
        responses.patch(
            "https://api.doppler.com/v3/workplace/groups/group/perferendis",
            json={},
            status=404,
        )
        with self.assertRaises(ClientException):
            test_service = Groups("testkey")
            test_service.update("perferendis", {})
        responses.reset()

    @responses.activate
    def test_delete(self):
        # Mock the API response
        responses.delete(
            "https://api.doppler.com/v3/workplace/groups/group/veniam",
            json={},
            status=200,
        )
        # call the method to test
        test_service = Groups("testkey")
        response = test_service.delete("veniam")
        self.assertEqual(response, {})
        responses.reset(),

    @responses.activate
    def test_delete_required_fields_missing(self):
        # Mock the API response
        responses.delete(
            "https://api.doppler.com/v3/workplace/groups/group/fugiat",
            json={},
            status=202,
        )
        with self.assertRaises(TypeError):
            test_service = Groups("testkey")
            test_service.delete()
        responses.reset(),

    @responses.activate
    def test_delete_error_on_non_200(self):
        # Mock the API response
        responses.delete(
            "https://api.doppler.com/v3/workplace/groups/group/numquam",
            json={},
            status=404,
        )
        with self.assertRaises(ClientException):
            test_service = Groups("testkey")
            test_service.delete("numquam")
        responses.reset()

    @responses.activate
    def test_add_member(self):
        # Mock the API response
        responses.post(
            "https://api.doppler.com/v3/workplace/groups/group/est/members",
            json={},
            status=200,
        )
        # call the method to test
        test_service = Groups("testkey")
        response = test_service.add_member("est", {})
        self.assertEqual(response, {})
        responses.reset(),

    @responses.activate
    def test_add_member_required_fields_missing(self):
        # Mock the API response
        responses.post(
            "https://api.doppler.com/v3/workplace/groups/group/pariatur/members",
            json={},
            status=202,
        )
        with self.assertRaises(TypeError):
            test_service = Groups("testkey")
            test_service.add_member()
        responses.reset(),

    @responses.activate
    def test_add_member_error_on_non_200(self):
        # Mock the API response
        responses.post(
            "https://api.doppler.com/v3/workplace/groups/group/ut/members",
            json={},
            status=404,
        )
        with self.assertRaises(ClientException):
            test_service = Groups("testkey")
            test_service.add_member("ut", {})
        responses.reset()

    @responses.activate
    def test_delete_member(self):
        # Mock the API response
        responses.delete(
            "https://api.doppler.com/v3/workplace/groups/group/dolore/members/workplace_user/repudiandae",
            json={},
            status=200,
        )
        # call the method to test
        test_service = Groups("testkey")
        response = test_service.delete_member("repudiandae", "workplace_user", "dolore")
        self.assertEqual(response, {})
        responses.reset(),

    @responses.activate
    def test_delete_member_required_fields_missing(self):
        # Mock the API response
        responses.delete(
            "https://api.doppler.com/v3/workplace/groups/group/consectetur/members/workplace_user/a",
            json={},
            status=202,
        )
        with self.assertRaises(TypeError):
            test_service = Groups("testkey")
            test_service.delete_member()
        responses.reset(),

    @responses.activate
    def test_delete_member_error_on_non_200(self):
        # Mock the API response
        responses.delete(
            "https://api.doppler.com/v3/workplace/groups/group/deleniti/members/workplace_user/facilis",
            json={},
            status=404,
        )
        with self.assertRaises(ClientException):
            test_service = Groups("testkey")
            test_service.delete_member("facilis", "workplace_user", "deleniti")
        responses.reset()


if __name__ == "__main__":
    unittest.main()

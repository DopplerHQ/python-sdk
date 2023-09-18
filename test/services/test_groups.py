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
        response = test_service.list(3, 5)
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
            test_service.list(6, 2)
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
            "https://api.doppler.com/v3/workplace/groups/group/asperiores",
            json={},
            status=200,
        )
        # call the method to test
        test_service = Groups("testkey")
        response = test_service.get("asperiores")
        self.assertEqual(response, {})
        responses.reset(),

    @responses.activate
    def test_get_required_fields_missing(self):
        # Mock the API response
        responses.get(
            "https://api.doppler.com/v3/workplace/groups/group/sed", json={}, status=202
        )
        with self.assertRaises(TypeError):
            test_service = Groups("testkey")
            test_service.get()
        responses.reset(),

    @responses.activate
    def test_get_error_on_non_200(self):
        # Mock the API response
        responses.get(
            "https://api.doppler.com/v3/workplace/groups/group/repellendus",
            json={},
            status=404,
        )
        with self.assertRaises(ClientException):
            test_service = Groups("testkey")
            test_service.get("repellendus")
        responses.reset()

    @responses.activate
    def test_update(self):
        # Mock the API response
        responses.patch(
            "https://api.doppler.com/v3/workplace/groups/group/magnam",
            json={},
            status=200,
        )
        # call the method to test
        test_service = Groups("testkey")
        response = test_service.update("magnam", {})
        self.assertEqual(response, {})
        responses.reset(),

    @responses.activate
    def test_update_required_fields_missing(self):
        # Mock the API response
        responses.patch(
            "https://api.doppler.com/v3/workplace/groups/group/laboriosam",
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
            "https://api.doppler.com/v3/workplace/groups/group/numquam",
            json={},
            status=404,
        )
        with self.assertRaises(ClientException):
            test_service = Groups("testkey")
            test_service.update("numquam", {})
        responses.reset()

    @responses.activate
    def test_delete(self):
        # Mock the API response
        responses.delete(
            "https://api.doppler.com/v3/workplace/groups/group/amet",
            json={},
            status=200,
        )
        # call the method to test
        test_service = Groups("testkey")
        response = test_service.delete("amet")
        self.assertEqual(response, {})
        responses.reset(),

    @responses.activate
    def test_delete_required_fields_missing(self):
        # Mock the API response
        responses.delete(
            "https://api.doppler.com/v3/workplace/groups/group/adipisci",
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
            "https://api.doppler.com/v3/workplace/groups/group/odit",
            json={},
            status=404,
        )
        with self.assertRaises(ClientException):
            test_service = Groups("testkey")
            test_service.delete("odit")
        responses.reset()

    @responses.activate
    def test_add_member(self):
        # Mock the API response
        responses.post(
            "https://api.doppler.com/v3/workplace/groups/group/ab/members",
            json={},
            status=200,
        )
        # call the method to test
        test_service = Groups("testkey")
        response = test_service.add_member("ab", {})
        self.assertEqual(response, {})
        responses.reset(),

    @responses.activate
    def test_add_member_required_fields_missing(self):
        # Mock the API response
        responses.post(
            "https://api.doppler.com/v3/workplace/groups/group/esse/members",
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
            "https://api.doppler.com/v3/workplace/groups/group/dolores/members",
            json={},
            status=404,
        )
        with self.assertRaises(ClientException):
            test_service = Groups("testkey")
            test_service.add_member("dolores", {})
        responses.reset()

    @responses.activate
    def test_delete_member(self):
        # Mock the API response
        responses.delete(
            "https://api.doppler.com/v3/workplace/groups/group/libero/members/workplace_user/repellendus",
            json={},
            status=200,
        )
        # call the method to test
        test_service = Groups("testkey")
        response = test_service.delete_member("repellendus", "workplace_user", "libero")
        self.assertEqual(response, {})
        responses.reset(),

    @responses.activate
    def test_delete_member_required_fields_missing(self):
        # Mock the API response
        responses.delete(
            "https://api.doppler.com/v3/workplace/groups/group/dicta/members/workplace_user/a",
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
            "https://api.doppler.com/v3/workplace/groups/group/fugiat/members/workplace_user/quos",
            json={},
            status=404,
        )
        with self.assertRaises(ClientException):
            test_service = Groups("testkey")
            test_service.delete_member("quos", "workplace_user", "fugiat")
        responses.reset()


if __name__ == "__main__":
    unittest.main()

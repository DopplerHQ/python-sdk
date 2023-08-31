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
        response = test_service.list(5, 8)
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
            test_service.list(1, 1)
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
            "https://api.doppler.com/v3/workplace/groups/group/omnis",
            json={},
            status=200,
        )
        # call the method to test
        test_service = Groups("testkey")
        response = test_service.get("omnis")
        self.assertEqual(response, {})
        responses.reset(),

    @responses.activate
    def test_get_required_fields_missing(self):
        # Mock the API response
        responses.get(
            "https://api.doppler.com/v3/workplace/groups/group/voluptates",
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
            "https://api.doppler.com/v3/workplace/groups/group/quam",
            json={},
            status=404,
        )
        with self.assertRaises(ClientException):
            test_service = Groups("testkey")
            test_service.get("quam")
        responses.reset()

    @responses.activate
    def test_update(self):
        # Mock the API response
        responses.patch(
            "https://api.doppler.com/v3/workplace/groups/group/repellendus",
            json={},
            status=200,
        )
        # call the method to test
        test_service = Groups("testkey")
        response = test_service.update("repellendus", {})
        self.assertEqual(response, {})
        responses.reset(),

    @responses.activate
    def test_update_required_fields_missing(self):
        # Mock the API response
        responses.patch(
            "https://api.doppler.com/v3/workplace/groups/group/voluptatum",
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
            "https://api.doppler.com/v3/workplace/groups/group/maxime",
            json={},
            status=404,
        )
        with self.assertRaises(ClientException):
            test_service = Groups("testkey")
            test_service.update("maxime", {})
        responses.reset()

    @responses.activate
    def test_delete(self):
        # Mock the API response
        responses.delete(
            "https://api.doppler.com/v3/workplace/groups/group/numquam",
            json={},
            status=200,
        )
        # call the method to test
        test_service = Groups("testkey")
        response = test_service.delete("numquam")
        self.assertEqual(response, {})
        responses.reset(),

    @responses.activate
    def test_delete_required_fields_missing(self):
        # Mock the API response
        responses.delete(
            "https://api.doppler.com/v3/workplace/groups/group/quaerat",
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
            "https://api.doppler.com/v3/workplace/groups/group/pariatur",
            json={},
            status=404,
        )
        with self.assertRaises(ClientException):
            test_service = Groups("testkey")
            test_service.delete("pariatur")
        responses.reset()

    @responses.activate
    def test_add_member(self):
        # Mock the API response
        responses.post(
            "https://api.doppler.com/v3/workplace/groups/group/neque/members",
            json={},
            status=200,
        )
        # call the method to test
        test_service = Groups("testkey")
        response = test_service.add_member("neque", {})
        self.assertEqual(response, {})
        responses.reset(),

    @responses.activate
    def test_add_member_required_fields_missing(self):
        # Mock the API response
        responses.post(
            "https://api.doppler.com/v3/workplace/groups/group/praesentium/members",
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
            "https://api.doppler.com/v3/workplace/groups/group/est/members",
            json={},
            status=404,
        )
        with self.assertRaises(ClientException):
            test_service = Groups("testkey")
            test_service.add_member("est", {})
        responses.reset()

    @responses.activate
    def test_delete_member(self):
        # Mock the API response
        responses.delete(
            "https://api.doppler.com/v3/workplace/groups/group/ab/members/workplace_user/distinctio",
            json={},
            status=200,
        )
        # call the method to test
        test_service = Groups("testkey")
        response = test_service.delete_member("distinctio", "workplace_user", "ab")
        self.assertEqual(response, {})
        responses.reset(),

    @responses.activate
    def test_delete_member_required_fields_missing(self):
        # Mock the API response
        responses.delete(
            "https://api.doppler.com/v3/workplace/groups/group/nemo/members/workplace_user/recusandae",
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
            "https://api.doppler.com/v3/workplace/groups/group/adipisci/members/workplace_user/corporis",
            json={},
            status=404,
        )
        with self.assertRaises(ClientException):
            test_service = Groups("testkey")
            test_service.delete_member("corporis", "workplace_user", "adipisci")
        responses.reset()


if __name__ == "__main__":
    unittest.main()

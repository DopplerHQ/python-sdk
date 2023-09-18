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
        response = test_service.list(2, 1)
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
            test_service.list(2, 2)
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
            "https://api.doppler.com/v3/workplace/groups/group/ab", json={}, status=200
        )
        # call the method to test
        test_service = Groups("testkey")
        response = test_service.get("ab")
        self.assertEqual(response, {})
        responses.reset(),

    @responses.activate
    def test_get_required_fields_missing(self):
        # Mock the API response
        responses.get(
            "https://api.doppler.com/v3/workplace/groups/group/aperiam",
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
            "https://api.doppler.com/v3/workplace/groups/group/dolores",
            json={},
            status=404,
        )
        with self.assertRaises(ClientException):
            test_service = Groups("testkey")
            test_service.get("dolores")
        responses.reset()

    @responses.activate
    def test_update(self):
        # Mock the API response
        responses.patch(
            "https://api.doppler.com/v3/workplace/groups/group/possimus",
            json={},
            status=200,
        )
        # call the method to test
        test_service = Groups("testkey")
        response = test_service.update("possimus", {})
        self.assertEqual(response, {})
        responses.reset(),

    @responses.activate
    def test_update_required_fields_missing(self):
        # Mock the API response
        responses.patch(
            "https://api.doppler.com/v3/workplace/groups/group/dicta",
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
            "https://api.doppler.com/v3/workplace/groups/group/unde",
            json={},
            status=404,
        )
        with self.assertRaises(ClientException):
            test_service = Groups("testkey")
            test_service.update("unde", {})
        responses.reset()

    @responses.activate
    def test_delete(self):
        # Mock the API response
        responses.delete(
            "https://api.doppler.com/v3/workplace/groups/group/dolore",
            json={},
            status=200,
        )
        # call the method to test
        test_service = Groups("testkey")
        response = test_service.delete("dolore")
        self.assertEqual(response, {})
        responses.reset(),

    @responses.activate
    def test_delete_required_fields_missing(self):
        # Mock the API response
        responses.delete(
            "https://api.doppler.com/v3/workplace/groups/group/voluptate",
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
            "https://api.doppler.com/v3/workplace/groups/group/deleniti",
            json={},
            status=404,
        )
        with self.assertRaises(ClientException):
            test_service = Groups("testkey")
            test_service.delete("deleniti")
        responses.reset()

    @responses.activate
    def test_add_member(self):
        # Mock the API response
        responses.post(
            "https://api.doppler.com/v3/workplace/groups/group/impedit/members",
            json={},
            status=200,
        )
        # call the method to test
        test_service = Groups("testkey")
        response = test_service.add_member("impedit", {})
        self.assertEqual(response, {})
        responses.reset(),

    @responses.activate
    def test_add_member_required_fields_missing(self):
        # Mock the API response
        responses.post(
            "https://api.doppler.com/v3/workplace/groups/group/nulla/members",
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
            "https://api.doppler.com/v3/workplace/groups/group/quam/members/workplace_user/facilis",
            json={},
            status=200,
        )
        # call the method to test
        test_service = Groups("testkey")
        response = test_service.delete_member("facilis", "workplace_user", "quam")
        self.assertEqual(response, {})
        responses.reset(),

    @responses.activate
    def test_delete_member_required_fields_missing(self):
        # Mock the API response
        responses.delete(
            "https://api.doppler.com/v3/workplace/groups/group/suscipit/members/workplace_user/accusantium",
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
            "https://api.doppler.com/v3/workplace/groups/group/dignissimos/members/workplace_user/unde",
            json={},
            status=404,
        )
        with self.assertRaises(ClientException):
            test_service = Groups("testkey")
            test_service.delete_member("unde", "workplace_user", "dignissimos")
        responses.reset()


if __name__ == "__main__":
    unittest.main()

import unittest
import responses
from src.dopplersdk.net.http_client import HTTPClient
from http_exceptions import ClientException
from src.dopplersdk.services.groups import Groups


class TestGroups_(unittest.TestCase):
    def test_true(self):
        self.assertTrue(True)

    @responses.activate
    def test_get(self):
        # Mock the API response
        responses.get(
            "https://api.doppler.com/v3/workplace/groups/group/expedita",
            json={},
            status=200,
        )
        # call the method to test
        test_service = Groups("testkey")
        response = test_service.get("expedita")
        self.assertEqual(response, {})
        responses.reset(),

    @responses.activate
    def test_get_required_fields_missing(self):
        # Mock the API response
        responses.get(
            "https://api.doppler.com/v3/workplace/groups/group/ex", json={}, status=202
        )
        with self.assertRaises(TypeError):
            test_service = Groups("testkey")
            test_service.get()
        responses.reset(),

    @responses.activate
    def test_get_error_on_non_200(self):
        # Mock the API response
        responses.get(
            "https://api.doppler.com/v3/workplace/groups/group/ratione",
            json={},
            status=404,
        )
        with self.assertRaises(ClientException):
            test_service = Groups("testkey")
            test_service.get("ratione")
        responses.reset()

    @responses.activate
    def test_update(self):
        # Mock the API response
        responses.patch(
            "https://api.doppler.com/v3/workplace/groups/group/consequuntur",
            json={},
            status=200,
        )
        # call the method to test
        test_service = Groups("testkey")
        response = test_service.update("consequuntur", {})
        self.assertEqual(response, {})
        responses.reset(),

    @responses.activate
    def test_update_required_fields_missing(self):
        # Mock the API response
        responses.patch(
            "https://api.doppler.com/v3/workplace/groups/group/occaecati",
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
            "https://api.doppler.com/v3/workplace/groups/group/ad", json={}, status=404
        )
        with self.assertRaises(ClientException):
            test_service = Groups("testkey")
            test_service.update("ad", {})
        responses.reset()

    @responses.activate
    def test_delete(self):
        # Mock the API response
        responses.delete(
            "https://api.doppler.com/v3/workplace/groups/group/et", json={}, status=200
        )
        # call the method to test
        test_service = Groups("testkey")
        response = test_service.delete("et")
        self.assertEqual(response, {})
        responses.reset(),

    @responses.activate
    def test_delete_required_fields_missing(self):
        # Mock the API response
        responses.delete(
            "https://api.doppler.com/v3/workplace/groups/group/amet",
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
            "https://api.doppler.com/v3/workplace/groups/group/a", json={}, status=404
        )
        with self.assertRaises(ClientException):
            test_service = Groups("testkey")
            test_service.delete("a")
        responses.reset()

    @responses.activate
    def test_list(self):
        # Mock the API response
        responses.get(
            "https://api.doppler.com/v3/workplace/groups", json={}, status=200
        )
        # call the method to test
        test_service = Groups("testkey")
        response = test_service.list(3, 1)
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
    def test_delete_member(self):
        # Mock the API response
        responses.delete(
            "https://api.doppler.com/v3/workplace/groups/group/quidem/members/workplace_user/voluptas",
            json={},
            status=200,
        )
        # call the method to test
        test_service = Groups("testkey")
        response = test_service.delete_member("voluptas", "workplace_user", "quidem")
        self.assertEqual(response, {})
        responses.reset(),

    @responses.activate
    def test_delete_member_required_fields_missing(self):
        # Mock the API response
        responses.delete(
            "https://api.doppler.com/v3/workplace/groups/group/temporibus/members/workplace_user/eum",
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
            "https://api.doppler.com/v3/workplace/groups/group/et/members/workplace_user/natus",
            json={},
            status=404,
        )
        with self.assertRaises(ClientException):
            test_service = Groups("testkey")
            test_service.delete_member("natus", "workplace_user", "et")
        responses.reset()

    @responses.activate
    def test_add_member(self):
        # Mock the API response
        responses.post(
            "https://api.doppler.com/v3/workplace/groups/group/dicta/members",
            json={},
            status=200,
        )
        # call the method to test
        test_service = Groups("testkey")
        response = test_service.add_member("dicta", {})
        self.assertEqual(response, {})
        responses.reset(),

    @responses.activate
    def test_add_member_required_fields_missing(self):
        # Mock the API response
        responses.post(
            "https://api.doppler.com/v3/workplace/groups/group/velit/members",
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
            "https://api.doppler.com/v3/workplace/groups/group/sequi/members",
            json={},
            status=404,
        )
        with self.assertRaises(ClientException):
            test_service = Groups("testkey")
            test_service.add_member("sequi", {})
        responses.reset()


if __name__ == "__main__":
    unittest.main()

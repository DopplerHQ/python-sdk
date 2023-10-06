import unittest
from src.dopplersdk.models.UsersGetResponse import UsersGetResponse


class TestUsersGetResponseModel(unittest.TestCase):
    def test_true(self):
        self.assertTrue(True)

    def test_users_get_response(self):
        # Create UsersGetResponse class instance
        test_model = UsersGetResponse(workplace_user={"repudiandae": 3}, success=True)
        self.assertEqual(test_model.workplace_user, {"repudiandae": 3})
        self.assertEqual(test_model.success, True)


if __name__ == "__main__":
    unittest.main()

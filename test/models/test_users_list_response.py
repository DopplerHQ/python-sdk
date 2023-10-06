import unittest
from src.dopplersdk.models.UsersListResponse import UsersListResponse


class TestUsersListResponseModel(unittest.TestCase):
    def test_true(self):
        self.assertTrue(True)

    def test_users_list_response(self):
        # Create UsersListResponse class instance
        test_model = UsersListResponse(
            workplace_users=["saepe", "dolorem"], page=9, success=True
        )
        self.assertEqual(test_model.workplace_users, ["saepe", "dolorem"])
        self.assertEqual(test_model.page, 9)
        self.assertEqual(test_model.success, True)


if __name__ == "__main__":
    unittest.main()

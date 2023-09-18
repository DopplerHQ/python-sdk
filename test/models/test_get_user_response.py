import unittest
from src.dopplersdk.models.GetUserResponse import GetUserResponse


class TestGetUserResponseModel(unittest.TestCase):
    def test_true(self):
        self.assertTrue(True)

    def test_get_user_response(self):
        # Create GetUserResponse class instance
        test_model = GetUserResponse(workplace_user={"quasi": 2}, success=True)
        self.assertEqual(test_model.workplace_user, {"quasi": 2})
        self.assertEqual(test_model.success, True)


if __name__ == "__main__":
    unittest.main()

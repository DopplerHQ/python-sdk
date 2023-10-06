import unittest
from src.dopplersdk.models.EnvironmentsListResponse import EnvironmentsListResponse


class TestEnvironmentsListResponseModel(unittest.TestCase):
    def test_true(self):
        self.assertTrue(True)

    def test_environments_list_response(self):
        # Create EnvironmentsListResponse class instance
        test_model = EnvironmentsListResponse(environments=["ipsa", "veniam"], page=5)
        self.assertEqual(test_model.environments, ["ipsa", "veniam"])
        self.assertEqual(test_model.page, 5)


if __name__ == "__main__":
    unittest.main()

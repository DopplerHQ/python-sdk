import unittest
from src.dopplersdk.models.EnvironmentsListResponse import EnvironmentsListResponse


class TestEnvironmentsListResponseModel(unittest.TestCase):
    def test_true(self):
        self.assertTrue(True)

    def test_environments_list_response(self):
        # Create EnvironmentsListResponse class instance
        test_model = EnvironmentsListResponse(
            environments=["tempore", "exercitationem"], page=1
        )
        self.assertEqual(test_model.environments, ["tempore", "exercitationem"])
        self.assertEqual(test_model.page, 1)


if __name__ == "__main__":
    unittest.main()

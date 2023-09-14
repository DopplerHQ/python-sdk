import unittest
from src.dopplersdk.models.EnvironmentsListResponse import EnvironmentsListResponse


class TestEnvironmentsListResponseModel(unittest.TestCase):
    def test_true(self):
        self.assertTrue(True)

    def test_environments_list_response(self):
        # Create EnvironmentsListResponse class instance
        test_model = EnvironmentsListResponse(
            environments=["tempora", "blanditiis"], page=9
        )
        self.assertEqual(test_model.environments, ["tempora", "blanditiis"])
        self.assertEqual(test_model.page, 9)


if __name__ == "__main__":
    unittest.main()

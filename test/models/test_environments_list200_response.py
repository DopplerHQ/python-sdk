import unittest
from src.dopplersdk.models.EnvironmentsList200Response import (
    EnvironmentsList200Response,
)


class TestEnvironmentsList200ResponseModel(unittest.TestCase):
    def test_true(self):
        self.assertTrue(True)

    def test_environments_list200_response(self):
        # Create EnvironmentsList200Response class instance
        test_model = EnvironmentsList200Response(
            environments=["velit", "accusamus"], page=6
        )
        self.assertEqual(test_model.environments, ["velit", "accusamus"])
        self.assertEqual(test_model.page, 6)


if __name__ == "__main__":
    unittest.main()

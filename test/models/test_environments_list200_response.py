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
            environments=["blanditiis", "alias"], page=3
        )
        self.assertEqual(test_model.environments, ["blanditiis", "alias"])
        self.assertEqual(test_model.page, 3)


if __name__ == "__main__":
    unittest.main()

import unittest
from src.dopplersdk.models.EnvironmentsRename200Response import (
    EnvironmentsRename200Response,
)


class TestEnvironmentsRename200ResponseModel(unittest.TestCase):
    def test_true(self):
        self.assertTrue(True)

    def test_environments_rename200_response(self):
        # Create EnvironmentsRename200Response class instance
        test_model = EnvironmentsRename200Response(environment={"eum": 5})
        self.assertEqual(test_model.environment, {"eum": 5})


if __name__ == "__main__":
    unittest.main()

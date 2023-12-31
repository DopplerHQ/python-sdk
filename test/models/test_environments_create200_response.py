import unittest
from src.dopplersdk.models.EnvironmentsCreate200Response import (
    EnvironmentsCreate200Response,
)


class TestEnvironmentsCreate200ResponseModel(unittest.TestCase):
    def test_true(self):
        self.assertTrue(True)

    def test_environments_create200_response(self):
        # Create EnvironmentsCreate200Response class instance
        test_model = EnvironmentsCreate200Response(environment={"cum": 4})
        self.assertEqual(test_model.environment, {"cum": 4})


if __name__ == "__main__":
    unittest.main()

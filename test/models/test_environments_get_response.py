import unittest
from src.dopplersdk.models.EnvironmentsGetResponse import EnvironmentsGetResponse


class TestEnvironmentsGetResponseModel(unittest.TestCase):
    def test_true(self):
        self.assertTrue(True)

    def test_environments_get_response(self):
        # Create EnvironmentsGetResponse class instance
        test_model = EnvironmentsGetResponse(environment={"omnis": 5})
        self.assertEqual(test_model.environment, {"omnis": 5})


if __name__ == "__main__":
    unittest.main()

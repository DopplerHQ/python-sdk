import unittest
from src.dopplersdk.models.EnvironmentsGetResponse import EnvironmentsGetResponse


class TestEnvironmentsGetResponseModel(unittest.TestCase):
    def test_true(self):
        self.assertTrue(True)

    def test_environments_get_response(self):
        # Create EnvironmentsGetResponse class instance
        test_model = EnvironmentsGetResponse(environment={"delectus": 2})
        self.assertEqual(test_model.environment, {"delectus": 2})


if __name__ == "__main__":
    unittest.main()

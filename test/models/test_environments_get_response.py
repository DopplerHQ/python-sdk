import unittest
from src.dopplersdk.models.EnvironmentsGetResponse import EnvironmentsGetResponse


class TestEnvironmentsGetResponseModel(unittest.TestCase):
    def test_true(self):
        self.assertTrue(True)

    def test_environments_get_response(self):
        # Create EnvironmentsGetResponse class instance
        test_model = EnvironmentsGetResponse(environment={"ad": 9})
        self.assertEqual(test_model.environment, {"ad": 9})


if __name__ == "__main__":
    unittest.main()

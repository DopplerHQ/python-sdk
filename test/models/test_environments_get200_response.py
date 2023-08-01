import unittest
from src.dopplersdk.models.EnvironmentsGet200Response import EnvironmentsGet200Response


class TestEnvironmentsGet200ResponseModel(unittest.TestCase):
    def test_true(self):
        self.assertTrue(True)

    def test_environments_get200_response(self):
        # Create EnvironmentsGet200Response class instance
        test_model = EnvironmentsGet200Response(environment={"eos": 8})
        self.assertEqual(test_model.environment, {"eos": 8})


if __name__ == "__main__":
    unittest.main()

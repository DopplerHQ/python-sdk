import unittest
from src.dopplersdk.models.EnvironmentsCreateResponse import EnvironmentsCreateResponse


class TestEnvironmentsCreateResponseModel(unittest.TestCase):
    def test_true(self):
        self.assertTrue(True)

    def test_environments_create_response(self):
        # Create EnvironmentsCreateResponse class instance
        test_model = EnvironmentsCreateResponse(environment={"modi": 1})
        self.assertEqual(test_model.environment, {"modi": 1})


if __name__ == "__main__":
    unittest.main()

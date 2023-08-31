import unittest
from src.dopplersdk.models.CreateRequest import CreateRequest


class TestCreateRequestModel(unittest.TestCase):
    def test_true(self):
        self.assertTrue(True)

    def test_create_request(self):
        # Create CreateRequest class instance
        test_model = CreateRequest(name="explicabo", default_project_role="eveniet")
        self.assertEqual(test_model.name, "explicabo")
        self.assertEqual(test_model.default_project_role, "eveniet")

    def test_create_request_required_fields_missing(self):
        # Assert CreateRequest class generation fails without required fields
        with self.assertRaises(TypeError):
            test_model = CreateRequest()


if __name__ == "__main__":
    unittest.main()

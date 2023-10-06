import unittest
from src.dopplersdk.models.CreateRequest import CreateRequest


class TestCreateRequestModel(unittest.TestCase):
    def test_true(self):
        self.assertTrue(True)

    def test_create_request(self):
        # Create CreateRequest class instance
        test_model = CreateRequest(name="corporis", description="animi")
        self.assertEqual(test_model.name, "corporis")
        self.assertEqual(test_model.description, "animi")

    def test_create_request_required_fields_missing(self):
        # Assert CreateRequest class generation fails without required fields
        with self.assertRaises(TypeError):
            test_model = CreateRequest()


if __name__ == "__main__":
    unittest.main()

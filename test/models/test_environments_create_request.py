import unittest
from src.dopplersdk.models.EnvironmentsCreateRequest import EnvironmentsCreateRequest


class TestEnvironmentsCreateRequestModel(unittest.TestCase):
    def test_true(self):
        self.assertTrue(True)

    def test_environments_create_request(self):
        # Create EnvironmentsCreateRequest class instance
        test_model = EnvironmentsCreateRequest(slug="nemo", name="eos")
        self.assertEqual(test_model.slug, "nemo")
        self.assertEqual(test_model.name, "eos")

    def test_environments_create_request_required_fields_missing(self):
        # Assert EnvironmentsCreateRequest class generation fails without required fields
        with self.assertRaises(TypeError):
            test_model = EnvironmentsCreateRequest()


if __name__ == "__main__":
    unittest.main()

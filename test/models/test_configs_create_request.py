import unittest
from src.dopplersdk.models.ConfigsCreateRequest import ConfigsCreateRequest


class TestConfigsCreateRequestModel(unittest.TestCase):
    def test_true(self):
        self.assertTrue(True)

    def test_configs_create_request(self):
        # Create ConfigsCreateRequest class instance
        test_model = ConfigsCreateRequest(
            name="dolor", environment="mollitia", project="cum"
        )
        self.assertEqual(test_model.name, "dolor")
        self.assertEqual(test_model.environment, "mollitia")
        self.assertEqual(test_model.project, "cum")

    def test_configs_create_request_required_fields_missing(self):
        # Assert ConfigsCreateRequest class generation fails without required fields
        with self.assertRaises(TypeError):
            test_model = ConfigsCreateRequest()


if __name__ == "__main__":
    unittest.main()

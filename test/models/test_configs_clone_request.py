import unittest
from src.dopplersdk.models.ConfigsCloneRequest import ConfigsCloneRequest


class TestConfigsCloneRequestModel(unittest.TestCase):
    def test_true(self):
        self.assertTrue(True)

    def test_configs_clone_request(self):
        # Create ConfigsCloneRequest class instance
        test_model = ConfigsCloneRequest(name="amet", config="natus", project="et")
        self.assertEqual(test_model.name, "amet")
        self.assertEqual(test_model.config, "natus")
        self.assertEqual(test_model.project, "et")

    def test_configs_clone_request_required_fields_missing(self):
        # Assert ConfigsCloneRequest class generation fails without required fields
        with self.assertRaises(TypeError):
            test_model = ConfigsCloneRequest()


if __name__ == "__main__":
    unittest.main()

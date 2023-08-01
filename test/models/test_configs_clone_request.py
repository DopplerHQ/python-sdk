import unittest
from src.dopplersdk.models.ConfigsCloneRequest import ConfigsCloneRequest


class TestConfigsCloneRequestModel(unittest.TestCase):
    def test_true(self):
        self.assertTrue(True)

    def test_configs_clone_request(self):
        # Create ConfigsCloneRequest class instance
        test_model = ConfigsCloneRequest(
            name="laboriosam", config="inventore", project="unde"
        )
        self.assertEqual(test_model.name, "laboriosam")
        self.assertEqual(test_model.config, "inventore")
        self.assertEqual(test_model.project, "unde")

    def test_configs_clone_request_required_fields_missing(self):
        # Assert ConfigsCloneRequest class generation fails without required fields
        with self.assertRaises(TypeError):
            test_model = ConfigsCloneRequest()


if __name__ == "__main__":
    unittest.main()

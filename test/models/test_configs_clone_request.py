import unittest
from src.dopplersdk.models.ConfigsCloneRequest import ConfigsCloneRequest


class TestConfigsCloneRequestModel(unittest.TestCase):
    def test_true(self):
        self.assertTrue(True)

    def test_configs_clone_request(self):
        # Create ConfigsCloneRequest class instance
        test_model = ConfigsCloneRequest(
            name="molestiae", config="illo", project="iste"
        )
        self.assertEqual(test_model.name, "molestiae")
        self.assertEqual(test_model.config, "illo")
        self.assertEqual(test_model.project, "iste")

    def test_configs_clone_request_required_fields_missing(self):
        # Assert ConfigsCloneRequest class generation fails without required fields
        with self.assertRaises(TypeError):
            test_model = ConfigsCloneRequest()


if __name__ == "__main__":
    unittest.main()

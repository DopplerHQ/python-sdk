import unittest
from src.dopplersdk.models.ConfigsCloneRequest import ConfigsCloneRequest


class TestConfigsCloneRequestModel(unittest.TestCase):
    def test_true(self):
        self.assertTrue(True)

    def test_configs_clone_request(self):
        # Create ConfigsCloneRequest class instance
        test_model = ConfigsCloneRequest(
            name="cupiditate", config="nesciunt", project="eligendi"
        )
        self.assertEqual(test_model.name, "cupiditate")
        self.assertEqual(test_model.config, "nesciunt")
        self.assertEqual(test_model.project, "eligendi")

    def test_configs_clone_request_required_fields_missing(self):
        # Assert ConfigsCloneRequest class generation fails without required fields
        with self.assertRaises(TypeError):
            test_model = ConfigsCloneRequest()


if __name__ == "__main__":
    unittest.main()

import unittest
from src.dopplersdk.models.ConfigsUpdateRequest import ConfigsUpdateRequest


class TestConfigsUpdateRequestModel(unittest.TestCase):
    def test_true(self):
        self.assertTrue(True)

    def test_configs_update_request(self):
        # Create ConfigsUpdateRequest class instance
        test_model = ConfigsUpdateRequest(
            name="dolores", config="doloribus", project="repudiandae"
        )
        self.assertEqual(test_model.name, "dolores")
        self.assertEqual(test_model.config, "doloribus")
        self.assertEqual(test_model.project, "repudiandae")

    def test_configs_update_request_required_fields_missing(self):
        # Assert ConfigsUpdateRequest class generation fails without required fields
        with self.assertRaises(TypeError):
            test_model = ConfigsUpdateRequest()


if __name__ == "__main__":
    unittest.main()

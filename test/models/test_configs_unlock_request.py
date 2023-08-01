import unittest
from src.dopplersdk.models.ConfigsUnlockRequest import ConfigsUnlockRequest


class TestConfigsUnlockRequestModel(unittest.TestCase):
    def test_true(self):
        self.assertTrue(True)

    def test_configs_unlock_request(self):
        # Create ConfigsUnlockRequest class instance
        test_model = ConfigsUnlockRequest(config="veritatis", project="repellendus")
        self.assertEqual(test_model.config, "veritatis")
        self.assertEqual(test_model.project, "repellendus")

    def test_configs_unlock_request_required_fields_missing(self):
        # Assert ConfigsUnlockRequest class generation fails without required fields
        with self.assertRaises(TypeError):
            test_model = ConfigsUnlockRequest()


if __name__ == "__main__":
    unittest.main()

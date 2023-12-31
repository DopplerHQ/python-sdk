import unittest
from src.dopplersdk.models.ConfigsLockRequest import ConfigsLockRequest


class TestConfigsLockRequestModel(unittest.TestCase):
    def test_true(self):
        self.assertTrue(True)

    def test_configs_lock_request(self):
        # Create ConfigsLockRequest class instance
        test_model = ConfigsLockRequest(config="nulla", project="beatae")
        self.assertEqual(test_model.config, "nulla")
        self.assertEqual(test_model.project, "beatae")

    def test_configs_lock_request_required_fields_missing(self):
        # Assert ConfigsLockRequest class generation fails without required fields
        with self.assertRaises(TypeError):
            test_model = ConfigsLockRequest()


if __name__ == "__main__":
    unittest.main()

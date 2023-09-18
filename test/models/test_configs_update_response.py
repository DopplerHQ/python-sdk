import unittest
from src.dopplersdk.models.ConfigsUpdateResponse import ConfigsUpdateResponse


class TestConfigsUpdateResponseModel(unittest.TestCase):
    def test_true(self):
        self.assertTrue(True)

    def test_configs_update_response(self):
        # Create ConfigsUpdateResponse class instance
        test_model = ConfigsUpdateResponse(config={"quas": 5})
        self.assertEqual(test_model.config, {"quas": 5})


if __name__ == "__main__":
    unittest.main()

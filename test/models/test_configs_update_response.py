import unittest
from src.dopplersdk.models.ConfigsUpdateResponse import ConfigsUpdateResponse


class TestConfigsUpdateResponseModel(unittest.TestCase):
    def test_true(self):
        self.assertTrue(True)

    def test_configs_update_response(self):
        # Create ConfigsUpdateResponse class instance
        test_model = ConfigsUpdateResponse(config={"repellat": 8})
        self.assertEqual(test_model.config, {"repellat": 8})


if __name__ == "__main__":
    unittest.main()

import unittest
from src.dopplersdk.models.ConfigsUnlock200Response import ConfigsUnlock200Response


class TestConfigsUnlock200ResponseModel(unittest.TestCase):
    def test_true(self):
        self.assertTrue(True)

    def test_configs_unlock200_response(self):
        # Create ConfigsUnlock200Response class instance
        test_model = ConfigsUnlock200Response(config={"odit": 9})
        self.assertEqual(test_model.config, {"odit": 9})


if __name__ == "__main__":
    unittest.main()

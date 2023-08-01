import unittest
from src.dopplersdk.models.ConfigsLock200Response import ConfigsLock200Response


class TestConfigsLock200ResponseModel(unittest.TestCase):
    def test_true(self):
        self.assertTrue(True)

    def test_configs_lock200_response(self):
        # Create ConfigsLock200Response class instance
        test_model = ConfigsLock200Response(config={"occaecati": 9})
        self.assertEqual(test_model.config, {"occaecati": 9})


if __name__ == "__main__":
    unittest.main()

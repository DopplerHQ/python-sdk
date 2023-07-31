import unittest
from src.dopplersdk.models.ConfigsLock200Response import ConfigsLock200Response


class TestConfigsLock200ResponseModel(unittest.TestCase):
    def test_true(self):
        self.assertTrue(True)

    def test_configs_lock200_response(self):
        # Create ConfigsLock200Response class instance
        test_model = ConfigsLock200Response(config={"ea": 7})
        self.assertEqual(test_model.config, {"ea": 7})


if __name__ == "__main__":
    unittest.main()

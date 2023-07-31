import unittest
from src.dopplersdk.models.ConfigsLock200Response import ConfigsLock200Response


class TestConfigsLock200ResponseModel(unittest.TestCase):
    def test_true(self):
        self.assertTrue(True)

    def test_configs_lock200_response(self):
        # Create ConfigsLock200Response class instance
        test_model = ConfigsLock200Response(config={"aliquam": 4})
        self.assertEqual(test_model.config, {"aliquam": 4})


if __name__ == "__main__":
    unittest.main()

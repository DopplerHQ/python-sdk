import unittest
from src.dopplersdk.models.ConfigsClone200Response import ConfigsClone200Response


class TestConfigsClone200ResponseModel(unittest.TestCase):
    def test_true(self):
        self.assertTrue(True)

    def test_configs_clone200_response(self):
        # Create ConfigsClone200Response class instance
        test_model = ConfigsClone200Response(config={"minima": 7})
        self.assertEqual(test_model.config, {"minima": 7})


if __name__ == "__main__":
    unittest.main()

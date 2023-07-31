import unittest
from src.dopplersdk.models.ConfigsList200Response import ConfigsList200Response


class TestConfigsList200ResponseModel(unittest.TestCase):
    def test_true(self):
        self.assertTrue(True)

    def test_configs_list200_response(self):
        # Create ConfigsList200Response class instance
        test_model = ConfigsList200Response(page=3, configs=["minima", "cum"])
        self.assertEqual(test_model.page, 3)
        self.assertEqual(test_model.configs, ["minima", "cum"])


if __name__ == "__main__":
    unittest.main()

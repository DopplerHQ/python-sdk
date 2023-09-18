import unittest
from src.dopplersdk.models.ConfigsListResponse import ConfigsListResponse


class TestConfigsListResponseModel(unittest.TestCase):
    def test_true(self):
        self.assertTrue(True)

    def test_configs_list_response(self):
        # Create ConfigsListResponse class instance
        test_model = ConfigsListResponse(page=2, configs=["expedita", "eius"])
        self.assertEqual(test_model.page, 2)
        self.assertEqual(test_model.configs, ["expedita", "eius"])


if __name__ == "__main__":
    unittest.main()

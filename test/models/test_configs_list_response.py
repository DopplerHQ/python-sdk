import unittest
from src.dopplersdk.models.ConfigsListResponse import ConfigsListResponse


class TestConfigsListResponseModel(unittest.TestCase):
    def test_true(self):
        self.assertTrue(True)

    def test_configs_list_response(self):
        # Create ConfigsListResponse class instance
        test_model = ConfigsListResponse(page=1, configs=["perferendis", "magnam"])
        self.assertEqual(test_model.page, 1)
        self.assertEqual(test_model.configs, ["perferendis", "magnam"])


if __name__ == "__main__":
    unittest.main()

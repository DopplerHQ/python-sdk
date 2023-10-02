import unittest
from src.dopplersdk.models.ConfigLogsListResponse import ConfigLogsListResponse


class TestConfigLogsListResponseModel(unittest.TestCase):
    def test_true(self):
        self.assertTrue(True)

    def test_config_logs_list_response(self):
        # Create ConfigLogsListResponse class instance
        test_model = ConfigLogsListResponse(page=5, logs=["quia", "itaque"])
        self.assertEqual(test_model.page, 5)
        self.assertEqual(test_model.logs, ["quia", "itaque"])


if __name__ == "__main__":
    unittest.main()

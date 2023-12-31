import unittest
from src.dopplersdk.models.ConfigLogsGet200Response import ConfigLogsGet200Response


class TestConfigLogsGet200ResponseModel(unittest.TestCase):
    def test_true(self):
        self.assertTrue(True)

    def test_config_logs_get200_response(self):
        # Create ConfigLogsGet200Response class instance
        test_model = ConfigLogsGet200Response(log={"quidem": 6})
        self.assertEqual(test_model.log, {"quidem": 6})


if __name__ == "__main__":
    unittest.main()

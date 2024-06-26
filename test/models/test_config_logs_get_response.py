import unittest
from src.dopplersdk.models.ConfigLogsGetResponse import ConfigLogsGetResponse


class TestConfigLogsGetResponseModel(unittest.TestCase):
    def test_true(self):
        self.assertTrue(True)

    def test_config_logs_get_response(self):
        # Create ConfigLogsGetResponse class instance
        test_model = ConfigLogsGetResponse(log={"reiciendis": 4})
        self.assertEqual(test_model.log, {"reiciendis": 4})


if __name__ == "__main__":
    unittest.main()

import unittest
from src.dopplersdk.models.ConfigLogsRollback200Response import (
    ConfigLogsRollback200Response,
)


class TestConfigLogsRollback200ResponseModel(unittest.TestCase):
    def test_true(self):
        self.assertTrue(True)

    def test_config_logs_rollback200_response(self):
        # Create ConfigLogsRollback200Response class instance
        test_model = ConfigLogsRollback200Response(log={"molestias": 4})
        self.assertEqual(test_model.log, {"molestias": 4})


if __name__ == "__main__":
    unittest.main()

import unittest
from src.dopplersdk.models.ConfigLogsList200Response import ConfigLogsList200Response


class TestConfigLogsList200ResponseModel(unittest.TestCase):
    def test_true(self):
        self.assertTrue(True)

    def test_config_logs_list200_response(self):
        # Create ConfigLogsList200Response class instance
        test_model = ConfigLogsList200Response(page=8, logs=["blanditiis", "minima"])
        self.assertEqual(test_model.page, 8)
        self.assertEqual(test_model.logs, ["blanditiis", "minima"])


if __name__ == "__main__":
    unittest.main()

import unittest
from src.dopplersdk.models.ConfigLogsList200Response import ConfigLogsList200Response


class TestConfigLogsList200ResponseModel(unittest.TestCase):
    def test_true(self):
        self.assertTrue(True)

    def test_config_logs_list200_response(self):
        # Create ConfigLogsList200Response class instance
        test_model = ConfigLogsList200Response(page=1, logs=["animi", "laudantium"])
        self.assertEqual(test_model.page, 1)
        self.assertEqual(test_model.logs, ["animi", "laudantium"])


if __name__ == "__main__":
    unittest.main()

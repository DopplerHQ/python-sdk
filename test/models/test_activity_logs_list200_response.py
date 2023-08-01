import unittest
from src.dopplersdk.models.ActivityLogsList200Response import (
    ActivityLogsList200Response,
)


class TestActivityLogsList200ResponseModel(unittest.TestCase):
    def test_true(self):
        self.assertTrue(True)

    def test_activity_logs_list200_response(self):
        # Create ActivityLogsList200Response class instance
        test_model = ActivityLogsList200Response(page=3, logs=["ipsa", "error"])
        self.assertEqual(test_model.page, 3)
        self.assertEqual(test_model.logs, ["ipsa", "error"])


if __name__ == "__main__":
    unittest.main()

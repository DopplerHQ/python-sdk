import unittest
from src.dopplersdk.models.ActivityLogsListResponse import ActivityLogsListResponse


class TestActivityLogsListResponseModel(unittest.TestCase):
    def test_true(self):
        self.assertTrue(True)

    def test_activity_logs_list_response(self):
        # Create ActivityLogsListResponse class instance
        test_model = ActivityLogsListResponse(page=2, logs=["itaque", "amet"])
        self.assertEqual(test_model.page, 2)
        self.assertEqual(test_model.logs, ["itaque", "amet"])


if __name__ == "__main__":
    unittest.main()

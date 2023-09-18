import unittest
from src.dopplersdk.models.ActivityLogsListResponse import ActivityLogsListResponse


class TestActivityLogsListResponseModel(unittest.TestCase):
    def test_true(self):
        self.assertTrue(True)

    def test_activity_logs_list_response(self):
        # Create ActivityLogsListResponse class instance
        test_model = ActivityLogsListResponse(page=7, logs=["recusandae", "ipsa"])
        self.assertEqual(test_model.page, 7)
        self.assertEqual(test_model.logs, ["recusandae", "ipsa"])


if __name__ == "__main__":
    unittest.main()

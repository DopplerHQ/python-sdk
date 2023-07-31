import unittest
from src.dopplersdk.models.ActivityLogsRetrieve200Response import (
    ActivityLogsRetrieve200Response,
)


class TestActivityLogsRetrieve200ResponseModel(unittest.TestCase):
    def test_true(self):
        self.assertTrue(True)

    def test_activity_logs_retrieve200_response(self):
        # Create ActivityLogsRetrieve200Response class instance
        test_model = ActivityLogsRetrieve200Response(log={"voluptatum": 6})
        self.assertEqual(test_model.log, {"voluptatum": 6})


if __name__ == "__main__":
    unittest.main()

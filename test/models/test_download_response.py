import unittest
from src.dopplersdk.models.DownloadResponse import DownloadResponse


class TestDownloadResponseModel(unittest.TestCase):
    def test_true(self):
        self.assertTrue(True)

    def test_download_response(self):
        # Create DownloadResponse class instance
        test_model = DownloadResponse(
            STRIPE="commodi", ALGOLIA="repellat", DATABASE="laborum", USER="error"
        )
        self.assertEqual(test_model.STRIPE, "commodi")
        self.assertEqual(test_model.ALGOLIA, "repellat")
        self.assertEqual(test_model.DATABASE, "laborum")
        self.assertEqual(test_model.USER, "error")


if __name__ == "__main__":
    unittest.main()

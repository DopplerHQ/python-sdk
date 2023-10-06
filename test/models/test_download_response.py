import unittest
from src.dopplersdk.models.DownloadResponse import DownloadResponse


class TestDownloadResponseModel(unittest.TestCase):
    def test_true(self):
        self.assertTrue(True)

    def test_download_response(self):
        # Create DownloadResponse class instance
        test_model = DownloadResponse(
            STRIPE="necessitatibus", ALGOLIA="totam", DATABASE="placeat", USER="error"
        )
        self.assertEqual(test_model.STRIPE, "necessitatibus")
        self.assertEqual(test_model.ALGOLIA, "totam")
        self.assertEqual(test_model.DATABASE, "placeat")
        self.assertEqual(test_model.USER, "error")


if __name__ == "__main__":
    unittest.main()

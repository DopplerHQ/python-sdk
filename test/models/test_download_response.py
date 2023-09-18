import unittest
from src.dopplersdk.models.DownloadResponse import DownloadResponse


class TestDownloadResponseModel(unittest.TestCase):
    def test_true(self):
        self.assertTrue(True)

    def test_download_response(self):
        # Create DownloadResponse class instance
        test_model = DownloadResponse(
            STRIPE="laudantium", ALGOLIA="hic", DATABASE="odit", USER="ab"
        )
        self.assertEqual(test_model.STRIPE, "laudantium")
        self.assertEqual(test_model.ALGOLIA, "hic")
        self.assertEqual(test_model.DATABASE, "odit")
        self.assertEqual(test_model.USER, "ab")


if __name__ == "__main__":
    unittest.main()

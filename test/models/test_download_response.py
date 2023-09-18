import unittest
from src.dopplersdk.models.DownloadResponse import DownloadResponse


class TestDownloadResponseModel(unittest.TestCase):
    def test_true(self):
        self.assertTrue(True)

    def test_download_response(self):
        # Create DownloadResponse class instance
        test_model = DownloadResponse(
            STRIPE="vero", ALGOLIA="libero", DATABASE="neque", USER="unde"
        )
        self.assertEqual(test_model.STRIPE, "vero")
        self.assertEqual(test_model.ALGOLIA, "libero")
        self.assertEqual(test_model.DATABASE, "neque")
        self.assertEqual(test_model.USER, "unde")


if __name__ == "__main__":
    unittest.main()

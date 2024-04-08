import unittest
from src.dopplersdk.models.DownloadResponse import DownloadResponse


class TestDownloadResponseModel(unittest.TestCase):
    def test_true(self):
        self.assertTrue(True)

    def test_download_response(self):
        # Create DownloadResponse class instance
        test_model = DownloadResponse(
            STRIPE="voluptatum", ALGOLIA="expedita", DATABASE="excepturi", USER="iste"
        )
        self.assertEqual(test_model.STRIPE, "voluptatum")
        self.assertEqual(test_model.ALGOLIA, "expedita")
        self.assertEqual(test_model.DATABASE, "excepturi")
        self.assertEqual(test_model.USER, "iste")


if __name__ == "__main__":
    unittest.main()

import unittest
from src.dopplersdk.models.DownloadResponse import DownloadResponse


class TestDownloadResponseModel(unittest.TestCase):
    def test_true(self):
        self.assertTrue(True)

    def test_download_response(self):
        # Create DownloadResponse class instance
        test_model = DownloadResponse(
            STRIPE="inventore", ALGOLIA="ea", DATABASE="quisquam", USER="excepturi"
        )
        self.assertEqual(test_model.STRIPE, "inventore")
        self.assertEqual(test_model.ALGOLIA, "ea")
        self.assertEqual(test_model.DATABASE, "quisquam")
        self.assertEqual(test_model.USER, "excepturi")


if __name__ == "__main__":
    unittest.main()

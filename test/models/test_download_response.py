import unittest
from src.dopplersdk.models.DownloadResponse import DownloadResponse


class TestDownloadResponseModel(unittest.TestCase):
    def test_true(self):
        self.assertTrue(True)

    def test_download_response(self):
        # Create DownloadResponse class instance
        test_model = DownloadResponse(
            STRIPE="impedit", ALGOLIA="esse", DATABASE="nulla", USER="ratione"
        )
        self.assertEqual(test_model.STRIPE, "impedit")
        self.assertEqual(test_model.ALGOLIA, "esse")
        self.assertEqual(test_model.DATABASE, "nulla")
        self.assertEqual(test_model.USER, "ratione")


if __name__ == "__main__":
    unittest.main()

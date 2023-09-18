import unittest
from src.dopplersdk.models.DownloadResponse import DownloadResponse


class TestDownloadResponseModel(unittest.TestCase):
    def test_true(self):
        self.assertTrue(True)

    def test_download_response(self):
        # Create DownloadResponse class instance
        test_model = DownloadResponse(
            STRIPE="magnam", ALGOLIA="veritatis", DATABASE="voluptatibus", USER="iure"
        )
        self.assertEqual(test_model.STRIPE, "magnam")
        self.assertEqual(test_model.ALGOLIA, "veritatis")
        self.assertEqual(test_model.DATABASE, "voluptatibus")
        self.assertEqual(test_model.USER, "iure")


if __name__ == "__main__":
    unittest.main()

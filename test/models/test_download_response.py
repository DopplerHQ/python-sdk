import unittest
from src.dopplersdk.models.DownloadResponse import DownloadResponse


class TestDownloadResponseModel(unittest.TestCase):
    def test_true(self):
        self.assertTrue(True)

    def test_download_response(self):
        # Create DownloadResponse class instance
        test_model = DownloadResponse(
            STRIPE="fugit", ALGOLIA="ut", DATABASE="aliquam", USER="voluptatum"
        )
        self.assertEqual(test_model.STRIPE, "fugit")
        self.assertEqual(test_model.ALGOLIA, "ut")
        self.assertEqual(test_model.DATABASE, "aliquam")
        self.assertEqual(test_model.USER, "voluptatum")


if __name__ == "__main__":
    unittest.main()

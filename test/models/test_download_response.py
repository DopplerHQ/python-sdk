import unittest
from src.dopplersdk.models.DownloadResponse import DownloadResponse


class TestDownloadResponseModel(unittest.TestCase):
    def test_true(self):
        self.assertTrue(True)

    def test_download_response(self):
        # Create DownloadResponse class instance
        test_model = DownloadResponse(
            STRIPE="officiis",
            ALGOLIA="consequuntur",
            DATABASE="fugit",
            USER="voluptate",
        )
        self.assertEqual(test_model.STRIPE, "officiis")
        self.assertEqual(test_model.ALGOLIA, "consequuntur")
        self.assertEqual(test_model.DATABASE, "fugit")
        self.assertEqual(test_model.USER, "voluptate")


if __name__ == "__main__":
    unittest.main()

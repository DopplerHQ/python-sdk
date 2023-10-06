import unittest
from src.dopplersdk.models.DownloadResponse import DownloadResponse


class TestDownloadResponseModel(unittest.TestCase):
    def test_true(self):
        self.assertTrue(True)

    def test_download_response(self):
        # Create DownloadResponse class instance
        test_model = DownloadResponse(
            STRIPE="consequuntur", ALGOLIA="expedita", DATABASE="officia", USER="vel"
        )
        self.assertEqual(test_model.STRIPE, "consequuntur")
        self.assertEqual(test_model.ALGOLIA, "expedita")
        self.assertEqual(test_model.DATABASE, "officia")
        self.assertEqual(test_model.USER, "vel")


if __name__ == "__main__":
    unittest.main()

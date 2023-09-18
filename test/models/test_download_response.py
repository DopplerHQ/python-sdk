import unittest
from src.dopplersdk.models.DownloadResponse import DownloadResponse


class TestDownloadResponseModel(unittest.TestCase):
    def test_true(self):
        self.assertTrue(True)

    def test_download_response(self):
        # Create DownloadResponse class instance
        test_model = DownloadResponse(
            STRIPE="ratione", ALGOLIA="porro", DATABASE="dicta", USER="dolorum"
        )
        self.assertEqual(test_model.STRIPE, "ratione")
        self.assertEqual(test_model.ALGOLIA, "porro")
        self.assertEqual(test_model.DATABASE, "dicta")
        self.assertEqual(test_model.USER, "dolorum")


if __name__ == "__main__":
    unittest.main()

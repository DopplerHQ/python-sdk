import unittest
from src.dopplersdk.models.SecretsDownload200Response import SecretsDownload200Response


class TestSecretsDownload200ResponseModel(unittest.TestCase):
    def test_true(self):
        self.assertTrue(True)

    def test_secrets_download200_response(self):
        # Create SecretsDownload200Response class instance
        test_model = SecretsDownload200Response(
            STRIPE="ea", ALGOLIA="architecto", DATABASE="minima", USER="qui"
        )
        self.assertEqual(test_model.STRIPE, "ea")
        self.assertEqual(test_model.ALGOLIA, "architecto")
        self.assertEqual(test_model.DATABASE, "minima")
        self.assertEqual(test_model.USER, "qui")


if __name__ == "__main__":
    unittest.main()

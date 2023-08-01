import unittest
from src.dopplersdk.models.SecretsDownload200Response import SecretsDownload200Response


class TestSecretsDownload200ResponseModel(unittest.TestCase):
    def test_true(self):
        self.assertTrue(True)

    def test_secrets_download200_response(self):
        # Create SecretsDownload200Response class instance
        test_model = SecretsDownload200Response(
            STRIPE="officiis", ALGOLIA="sit", DATABASE="provident", USER="atque"
        )
        self.assertEqual(test_model.STRIPE, "officiis")
        self.assertEqual(test_model.ALGOLIA, "sit")
        self.assertEqual(test_model.DATABASE, "provident")
        self.assertEqual(test_model.USER, "atque")


if __name__ == "__main__":
    unittest.main()

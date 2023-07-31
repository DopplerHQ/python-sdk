import unittest
from src.dopplersdk.models.SecretsDownload200Response import SecretsDownload200Response


class TestSecretsDownload200ResponseModel(unittest.TestCase):
    def test_true(self):
        self.assertTrue(True)

    def test_secrets_download200_response(self):
        # Create SecretsDownload200Response class instance
        test_model = SecretsDownload200Response(
            STRIPE="error",
            ALGOLIA="aspernatur",
            DATABASE="accusamus",
            USER="repellendus",
        )
        self.assertEqual(test_model.STRIPE, "error")
        self.assertEqual(test_model.ALGOLIA, "aspernatur")
        self.assertEqual(test_model.DATABASE, "accusamus")
        self.assertEqual(test_model.USER, "repellendus")


if __name__ == "__main__":
    unittest.main()

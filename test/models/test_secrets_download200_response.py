import unittest
from src.dopplersdk.models.SecretsDownload200Response import SecretsDownload200Response


class TestSecretsDownload200ResponseModel(unittest.TestCase):
    def test_true(self):
        self.assertTrue(True)

    def test_secrets_download200_response(self):
        # Create SecretsDownload200Response class instance
        test_model = SecretsDownload200Response(
            STRIPE="dolores", ALGOLIA="sint", DATABASE="rerum", USER="mollitia"
        )
        self.assertEqual(test_model.STRIPE, "dolores")
        self.assertEqual(test_model.ALGOLIA, "sint")
        self.assertEqual(test_model.DATABASE, "rerum")
        self.assertEqual(test_model.USER, "mollitia")


if __name__ == "__main__":
    unittest.main()

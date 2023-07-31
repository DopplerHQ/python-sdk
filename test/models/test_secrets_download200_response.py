import unittest
from src.dopplersdk.models.SecretsDownload200Response import SecretsDownload200Response


class TestSecretsDownload200ResponseModel(unittest.TestCase):
    def test_true(self):
        self.assertTrue(True)

    def test_secrets_download200_response(self):
        # Create SecretsDownload200Response class instance
        test_model = SecretsDownload200Response(
            STRIPE="sed", ALGOLIA="laborum", DATABASE="id", USER="minima"
        )
        self.assertEqual(test_model.STRIPE, "sed")
        self.assertEqual(test_model.ALGOLIA, "laborum")
        self.assertEqual(test_model.DATABASE, "id")
        self.assertEqual(test_model.USER, "minima")


if __name__ == "__main__":
    unittest.main()

import unittest
from src.dopplersdk.models.SecretsListResponse import SecretsListResponse


class TestSecretsListResponseModel(unittest.TestCase):
    def test_true(self):
        self.assertTrue(True)

    def test_secrets_list_response(self):
        # Create SecretsListResponse class instance
        test_model = SecretsListResponse(secrets={"omnis": 3})
        self.assertEqual(test_model.secrets, {"omnis": 3})


if __name__ == "__main__":
    unittest.main()

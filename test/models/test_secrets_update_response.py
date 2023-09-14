import unittest
from src.dopplersdk.models.SecretsUpdateResponse import SecretsUpdateResponse


class TestSecretsUpdateResponseModel(unittest.TestCase):
    def test_true(self):
        self.assertTrue(True)

    def test_secrets_update_response(self):
        # Create SecretsUpdateResponse class instance
        test_model = SecretsUpdateResponse(secrets={"odio": 2})
        self.assertEqual(test_model.secrets, {"odio": 2})


if __name__ == "__main__":
    unittest.main()

import unittest
from src.dopplersdk.models.SecretsUpdateResponse import SecretsUpdateResponse


class TestSecretsUpdateResponseModel(unittest.TestCase):
    def test_true(self):
        self.assertTrue(True)

    def test_secrets_update_response(self):
        # Create SecretsUpdateResponse class instance
        test_model = SecretsUpdateResponse(secrets={"recusandae": 9})
        self.assertEqual(test_model.secrets, {"recusandae": 9})


if __name__ == "__main__":
    unittest.main()

import unittest
from src.dopplersdk.models.SecretsUpdate200Response import SecretsUpdate200Response


class TestSecretsUpdate200ResponseModel(unittest.TestCase):
    def test_true(self):
        self.assertTrue(True)

    def test_secrets_update200_response(self):
        # Create SecretsUpdate200Response class instance
        test_model = SecretsUpdate200Response(secrets={"natus": 5})
        self.assertEqual(test_model.secrets, {"natus": 5})


if __name__ == "__main__":
    unittest.main()

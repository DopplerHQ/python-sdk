import unittest
from src.dopplersdk.models.SecretsUpdateNote200Response import (
    SecretsUpdateNote200Response,
)


class TestSecretsUpdateNote200ResponseModel(unittest.TestCase):
    def test_true(self):
        self.assertTrue(True)

    def test_secrets_update_note200_response(self):
        # Create SecretsUpdateNote200Response class instance
        test_model = SecretsUpdateNote200Response(secret="rerum", note="eligendi")
        self.assertEqual(test_model.secret, "rerum")
        self.assertEqual(test_model.note, "eligendi")


if __name__ == "__main__":
    unittest.main()

import unittest
from src.dopplersdk.models.SecretsGet200Response import SecretsGet200Response


class TestSecretsGet200ResponseModel(unittest.TestCase):
    def test_true(self):
        self.assertTrue(True)

    def test_secrets_get200_response(self):
        # Create SecretsGet200Response class instance
        test_model = SecretsGet200Response(name="dolorum", value={"iste": 6})
        self.assertEqual(test_model.name, "dolorum")
        self.assertEqual(test_model.value, {"iste": 6})


if __name__ == "__main__":
    unittest.main()

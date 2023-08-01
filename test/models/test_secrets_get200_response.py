import unittest
from src.dopplersdk.models.SecretsGet200Response import SecretsGet200Response


class TestSecretsGet200ResponseModel(unittest.TestCase):
    def test_true(self):
        self.assertTrue(True)

    def test_secrets_get200_response(self):
        # Create SecretsGet200Response class instance
        test_model = SecretsGet200Response(name="saepe", value={"sed": 4})
        self.assertEqual(test_model.name, "saepe")
        self.assertEqual(test_model.value, {"sed": 4})


if __name__ == "__main__":
    unittest.main()

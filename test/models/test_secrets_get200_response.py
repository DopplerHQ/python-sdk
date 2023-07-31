import unittest
from src.dopplersdk.models.SecretsGet200Response import SecretsGet200Response


class TestSecretsGet200ResponseModel(unittest.TestCase):
    def test_true(self):
        self.assertTrue(True)

    def test_secrets_get200_response(self):
        # Create SecretsGet200Response class instance
        test_model = SecretsGet200Response(name="labore", value={"placeat": 1})
        self.assertEqual(test_model.name, "labore")
        self.assertEqual(test_model.value, {"placeat": 1})


if __name__ == "__main__":
    unittest.main()

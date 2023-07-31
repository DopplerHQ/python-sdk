import unittest
from src.dopplersdk.models.SecretsGet200Response import SecretsGet200Response


class TestSecretsGet200ResponseModel(unittest.TestCase):
    def test_true(self):
        self.assertTrue(True)

    def test_secrets_get200_response(self):
        # Create SecretsGet200Response class instance
        test_model = SecretsGet200Response(name="nobis", value={"itaque": 8})
        self.assertEqual(test_model.name, "nobis")
        self.assertEqual(test_model.value, {"itaque": 8})


if __name__ == "__main__":
    unittest.main()

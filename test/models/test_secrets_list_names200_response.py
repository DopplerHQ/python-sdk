import unittest
from src.dopplersdk.models.SecretsListNames200Response import (
    SecretsListNames200Response,
)


class TestSecretsListNames200ResponseModel(unittest.TestCase):
    def test_true(self):
        self.assertTrue(True)

    def test_secrets_list_names200_response(self):
        # Create SecretsListNames200Response class instance
        test_model = SecretsListNames200Response(names=["optio", "minus"])
        self.assertEqual(test_model.names, ["optio", "minus"])


if __name__ == "__main__":
    unittest.main()

import unittest
from src.dopplersdk.models.SecretsGetResponse import SecretsGetResponse


class TestSecretsGetResponseModel(unittest.TestCase):
    def test_true(self):
        self.assertTrue(True)

    def test_secrets_get_response(self):
        # Create SecretsGetResponse class instance
        test_model = SecretsGetResponse(name="aliquid", value={"dolorum": 4})
        self.assertEqual(test_model.name, "aliquid")
        self.assertEqual(test_model.value, {"dolorum": 4})


if __name__ == "__main__":
    unittest.main()

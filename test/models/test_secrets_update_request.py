import unittest
from src.dopplersdk.models.SecretsUpdateRequest import SecretsUpdateRequest


class TestSecretsUpdateRequestModel(unittest.TestCase):
    def test_true(self):
        self.assertTrue(True)

    def test_secrets_update_request(self):
        # Create SecretsUpdateRequest class instance
        test_model = SecretsUpdateRequest(
            secrets={"assumenda": 8}, config="rerum", project="autem"
        )
        self.assertEqual(test_model.secrets, {"assumenda": 8})
        self.assertEqual(test_model.config, "rerum")
        self.assertEqual(test_model.project, "autem")

    def test_secrets_update_request_required_fields_missing(self):
        # Assert SecretsUpdateRequest class generation fails without required fields
        with self.assertRaises(TypeError):
            test_model = SecretsUpdateRequest()


if __name__ == "__main__":
    unittest.main()

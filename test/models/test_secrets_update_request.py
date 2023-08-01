import unittest
from src.dopplersdk.models.SecretsUpdateRequest import SecretsUpdateRequest


class TestSecretsUpdateRequestModel(unittest.TestCase):
    def test_true(self):
        self.assertTrue(True)

    def test_secrets_update_request(self):
        # Create SecretsUpdateRequest class instance
        test_model = SecretsUpdateRequest(
            secrets={"quos": 4}, config="ullam", project="consectetur"
        )
        self.assertEqual(test_model.secrets, {"quos": 4})
        self.assertEqual(test_model.config, "ullam")
        self.assertEqual(test_model.project, "consectetur")

    def test_secrets_update_request_required_fields_missing(self):
        # Assert SecretsUpdateRequest class generation fails without required fields
        with self.assertRaises(TypeError):
            test_model = SecretsUpdateRequest()


if __name__ == "__main__":
    unittest.main()

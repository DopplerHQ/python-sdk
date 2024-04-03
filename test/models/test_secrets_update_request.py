import unittest
from src.dopplersdk.models.SecretsUpdateRequest import SecretsUpdateRequest


class TestSecretsUpdateRequestModel(unittest.TestCase):
    def test_true(self):
        self.assertTrue(True)

    def test_secrets_update_request(self):
        # Create SecretsUpdateRequest class instance
        test_model = SecretsUpdateRequest(
            config="perspiciatis",
            project="id",
            secrets={"quod": 4},
            change_requests=["sit", "error"],
        )
        self.assertEqual(test_model.config, "perspiciatis")
        self.assertEqual(test_model.project, "id")
        self.assertEqual(test_model.secrets, {"quod": 4})
        self.assertEqual(test_model.change_requests, ["sit", "error"])

    def test_secrets_update_request_required_fields_missing(self):
        # Assert SecretsUpdateRequest class generation fails without required fields
        with self.assertRaises(TypeError):
            test_model = SecretsUpdateRequest()


if __name__ == "__main__":
    unittest.main()

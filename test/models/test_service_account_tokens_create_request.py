import unittest
from src.dopplersdk.models.ServiceAccountTokensCreateRequest import (
    ServiceAccountTokensCreateRequest,
)


class TestServiceAccountTokensCreateRequestModel(unittest.TestCase):
    def test_true(self):
        self.assertTrue(True)

    def test_service_account_tokens_create_request(self):
        # Create ServiceAccountTokensCreateRequest class instance
        test_model = ServiceAccountTokensCreateRequest(
            name="quam", expires_at="dolorem"
        )
        self.assertEqual(test_model.name, "quam")
        self.assertEqual(test_model.expires_at, "dolorem")


if __name__ == "__main__":
    unittest.main()

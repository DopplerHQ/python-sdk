import unittest
from src.dopplersdk.models.ServiceAccountTokensCreateResponse import (
    ServiceAccountTokensCreateResponse,
)


class TestServiceAccountTokensCreateResponseModel(unittest.TestCase):
    def test_true(self):
        self.assertTrue(True)

    def test_service_account_tokens_create_response(self):
        # Create ServiceAccountTokensCreateResponse class instance
        test_model = ServiceAccountTokensCreateResponse(
            api_token={"nulla": 4}, api_key="quas", success=True
        )
        self.assertEqual(test_model.api_token, {"nulla": 4})
        self.assertEqual(test_model.api_key, "quas")
        self.assertEqual(test_model.success, True)


if __name__ == "__main__":
    unittest.main()

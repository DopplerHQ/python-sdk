import unittest
from src.dopplersdk.models.ServiceAccountTokensGetResponse import (
    ServiceAccountTokensGetResponse,
)


class TestServiceAccountTokensGetResponseModel(unittest.TestCase):
    def test_true(self):
        self.assertTrue(True)

    def test_service_account_tokens_get_response(self):
        # Create ServiceAccountTokensGetResponse class instance
        test_model = ServiceAccountTokensGetResponse(
            api_token={"beatae": 7}, success=True
        )
        self.assertEqual(test_model.api_token, {"beatae": 7})
        self.assertEqual(test_model.success, True)


if __name__ == "__main__":
    unittest.main()

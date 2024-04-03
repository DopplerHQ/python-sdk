import unittest
from src.dopplersdk.models.ServiceAccountTokensListResponse import (
    ServiceAccountTokensListResponse,
)


class TestServiceAccountTokensListResponseModel(unittest.TestCase):
    def test_true(self):
        self.assertTrue(True)

    def test_service_account_tokens_list_response(self):
        # Create ServiceAccountTokensListResponse class instance
        test_model = ServiceAccountTokensListResponse(
            api_tokens=["doloribus", "corporis"], success=True
        )
        self.assertEqual(test_model.api_tokens, ["doloribus", "corporis"])
        self.assertEqual(test_model.success, True)


if __name__ == "__main__":
    unittest.main()

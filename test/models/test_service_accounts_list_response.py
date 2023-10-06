import unittest
from src.dopplersdk.models.ServiceAccountsListResponse import (
    ServiceAccountsListResponse,
)


class TestServiceAccountsListResponseModel(unittest.TestCase):
    def test_true(self):
        self.assertTrue(True)

    def test_service_accounts_list_response(self):
        # Create ServiceAccountsListResponse class instance
        test_model = ServiceAccountsListResponse(
            service_accounts=["inventore", "ducimus"]
        )
        self.assertEqual(test_model.service_accounts, ["inventore", "ducimus"])


if __name__ == "__main__":
    unittest.main()

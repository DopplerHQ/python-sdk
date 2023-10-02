import unittest
from src.dopplersdk.models.ServiceAccountsCreateResponse import (
    ServiceAccountsCreateResponse,
)


class TestServiceAccountsCreateResponseModel(unittest.TestCase):
    def test_true(self):
        self.assertTrue(True)

    def test_service_accounts_create_response(self):
        # Create ServiceAccountsCreateResponse class instance
        test_model = ServiceAccountsCreateResponse(service_account={"quia": 8})
        self.assertEqual(test_model.service_account, {"quia": 8})


if __name__ == "__main__":
    unittest.main()

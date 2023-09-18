import unittest
from src.dopplersdk.models.ServiceAccountsGetResponse import ServiceAccountsGetResponse


class TestServiceAccountsGetResponseModel(unittest.TestCase):
    def test_true(self):
        self.assertTrue(True)

    def test_service_accounts_get_response(self):
        # Create ServiceAccountsGetResponse class instance
        test_model = ServiceAccountsGetResponse(service_account={"soluta": 4})
        self.assertEqual(test_model.service_account, {"soluta": 4})


if __name__ == "__main__":
    unittest.main()

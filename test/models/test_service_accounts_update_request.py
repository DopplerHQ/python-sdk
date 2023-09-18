import unittest
from src.dopplersdk.models.ServiceAccountsUpdateRequest import (
    ServiceAccountsUpdateRequest,
)


class TestServiceAccountsUpdateRequestModel(unittest.TestCase):
    def test_true(self):
        self.assertTrue(True)

    def test_service_accounts_update_request(self):
        # Create ServiceAccountsUpdateRequest class instance
        test_model = ServiceAccountsUpdateRequest(
            name="laboriosam", workplace_role={"harum": 6}
        )
        self.assertEqual(test_model.name, "laboriosam")
        self.assertEqual(test_model.workplace_role, {"harum": 6})


if __name__ == "__main__":
    unittest.main()

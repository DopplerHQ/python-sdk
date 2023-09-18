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
            name="hic", workplace_role={"culpa": 7}
        )
        self.assertEqual(test_model.name, "hic")
        self.assertEqual(test_model.workplace_role, {"culpa": 7})


if __name__ == "__main__":
    unittest.main()

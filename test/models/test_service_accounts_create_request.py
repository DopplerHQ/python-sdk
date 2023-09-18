import unittest
from src.dopplersdk.models.ServiceAccountsCreateRequest import (
    ServiceAccountsCreateRequest,
)


class TestServiceAccountsCreateRequestModel(unittest.TestCase):
    def test_true(self):
        self.assertTrue(True)

    def test_service_accounts_create_request(self):
        # Create ServiceAccountsCreateRequest class instance
        test_model = ServiceAccountsCreateRequest(
            name="magni", workplace_role={"nam": 9}
        )
        self.assertEqual(test_model.name, "magni")
        self.assertEqual(test_model.workplace_role, {"nam": 9})


if __name__ == "__main__":
    unittest.main()

import unittest
from src.dopplersdk.models.WorkplaceUpdateRequest import WorkplaceUpdateRequest


class TestWorkplaceUpdateRequestModel(unittest.TestCase):
    def test_true(self):
        self.assertTrue(True)

    def test_workplace_update_request(self):
        # Create WorkplaceUpdateRequest class instance
        test_model = WorkplaceUpdateRequest(
            name="qui", billing_email="excepturi", security_email="ipsum"
        )
        self.assertEqual(test_model.name, "qui")
        self.assertEqual(test_model.billing_email, "excepturi")
        self.assertEqual(test_model.security_email, "ipsum")


if __name__ == "__main__":
    unittest.main()

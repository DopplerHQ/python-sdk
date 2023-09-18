import unittest
from src.dopplersdk.models.WorkplaceUpdateRequest import WorkplaceUpdateRequest


class TestWorkplaceUpdateRequestModel(unittest.TestCase):
    def test_true(self):
        self.assertTrue(True)

    def test_workplace_update_request(self):
        # Create WorkplaceUpdateRequest class instance
        test_model = WorkplaceUpdateRequest(
            name="quis", billing_email="voluptatum", security_email="quasi"
        )
        self.assertEqual(test_model.name, "quis")
        self.assertEqual(test_model.billing_email, "voluptatum")
        self.assertEqual(test_model.security_email, "quasi")


if __name__ == "__main__":
    unittest.main()

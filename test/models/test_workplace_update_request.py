import unittest
from src.dopplersdk.models.WorkplaceUpdateRequest import WorkplaceUpdateRequest


class TestWorkplaceUpdateRequestModel(unittest.TestCase):
    def test_true(self):
        self.assertTrue(True)

    def test_workplace_update_request(self):
        # Create WorkplaceUpdateRequest class instance
        test_model = WorkplaceUpdateRequest(
            name="minus", billing_email="rerum", security_email="error"
        )
        self.assertEqual(test_model.name, "minus")
        self.assertEqual(test_model.billing_email, "rerum")
        self.assertEqual(test_model.security_email, "error")


if __name__ == "__main__":
    unittest.main()

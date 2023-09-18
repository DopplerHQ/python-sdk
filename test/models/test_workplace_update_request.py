import unittest
from src.dopplersdk.models.WorkplaceUpdateRequest import WorkplaceUpdateRequest


class TestWorkplaceUpdateRequestModel(unittest.TestCase):
    def test_true(self):
        self.assertTrue(True)

    def test_workplace_update_request(self):
        # Create WorkplaceUpdateRequest class instance
        test_model = WorkplaceUpdateRequest(
            name="nobis", billing_email="eveniet", security_email="quia"
        )
        self.assertEqual(test_model.name, "nobis")
        self.assertEqual(test_model.billing_email, "eveniet")
        self.assertEqual(test_model.security_email, "quia")


if __name__ == "__main__":
    unittest.main()

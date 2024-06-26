import unittest
from src.dopplersdk.models.WorkplaceUpdateRequest import WorkplaceUpdateRequest


class TestWorkplaceUpdateRequestModel(unittest.TestCase):
    def test_true(self):
        self.assertTrue(True)

    def test_workplace_update_request(self):
        # Create WorkplaceUpdateRequest class instance
        test_model = WorkplaceUpdateRequest(
            name="eum", billing_email="saepe", security_email="placeat"
        )
        self.assertEqual(test_model.name, "eum")
        self.assertEqual(test_model.billing_email, "saepe")
        self.assertEqual(test_model.security_email, "placeat")


if __name__ == "__main__":
    unittest.main()

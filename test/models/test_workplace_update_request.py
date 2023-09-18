import unittest
from src.dopplersdk.models.WorkplaceUpdateRequest import WorkplaceUpdateRequest


class TestWorkplaceUpdateRequestModel(unittest.TestCase):
    def test_true(self):
        self.assertTrue(True)

    def test_workplace_update_request(self):
        # Create WorkplaceUpdateRequest class instance
        test_model = WorkplaceUpdateRequest(
            name="reprehenderit", billing_email="quam", security_email="deserunt"
        )
        self.assertEqual(test_model.name, "reprehenderit")
        self.assertEqual(test_model.billing_email, "quam")
        self.assertEqual(test_model.security_email, "deserunt")


if __name__ == "__main__":
    unittest.main()

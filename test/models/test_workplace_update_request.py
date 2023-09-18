import unittest
from src.dopplersdk.models.WorkplaceUpdateRequest import WorkplaceUpdateRequest


class TestWorkplaceUpdateRequestModel(unittest.TestCase):
    def test_true(self):
        self.assertTrue(True)

    def test_workplace_update_request(self):
        # Create WorkplaceUpdateRequest class instance
        test_model = WorkplaceUpdateRequest(
            name="dolorem", billing_email="molestiae", security_email="quae"
        )
        self.assertEqual(test_model.name, "dolorem")
        self.assertEqual(test_model.billing_email, "molestiae")
        self.assertEqual(test_model.security_email, "quae")


if __name__ == "__main__":
    unittest.main()

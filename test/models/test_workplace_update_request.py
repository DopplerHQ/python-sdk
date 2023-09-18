import unittest
from src.dopplersdk.models.WorkplaceUpdateRequest import WorkplaceUpdateRequest


class TestWorkplaceUpdateRequestModel(unittest.TestCase):
    def test_true(self):
        self.assertTrue(True)

    def test_workplace_update_request(self):
        # Create WorkplaceUpdateRequest class instance
        test_model = WorkplaceUpdateRequest(
            name="consequuntur", billing_email="quidem", security_email="vero"
        )
        self.assertEqual(test_model.name, "consequuntur")
        self.assertEqual(test_model.billing_email, "quidem")
        self.assertEqual(test_model.security_email, "vero")


if __name__ == "__main__":
    unittest.main()

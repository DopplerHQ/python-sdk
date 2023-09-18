import unittest
from src.dopplersdk.models.RevokeLeaseRequest import RevokeLeaseRequest


class TestRevokeLeaseRequestModel(unittest.TestCase):
    def test_true(self):
        self.assertTrue(True)

    def test_revoke_lease_request(self):
        # Create RevokeLeaseRequest class instance
        test_model = RevokeLeaseRequest(
            slug="id", dynamic_secret="veniam", config="cum", project="maiores"
        )
        self.assertEqual(test_model.slug, "id")
        self.assertEqual(test_model.dynamic_secret, "veniam")
        self.assertEqual(test_model.config, "cum")
        self.assertEqual(test_model.project, "maiores")

    def test_revoke_lease_request_required_fields_missing(self):
        # Assert RevokeLeaseRequest class generation fails without required fields
        with self.assertRaises(TypeError):
            test_model = RevokeLeaseRequest()


if __name__ == "__main__":
    unittest.main()

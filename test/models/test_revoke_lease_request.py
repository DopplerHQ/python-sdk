import unittest
from src.dopplersdk.models.RevokeLeaseRequest import RevokeLeaseRequest


class TestRevokeLeaseRequestModel(unittest.TestCase):
    def test_true(self):
        self.assertTrue(True)

    def test_revoke_lease_request(self):
        # Create RevokeLeaseRequest class instance
        test_model = RevokeLeaseRequest(
            slug="omnis",
            dynamic_secret="maiores",
            config="inventore",
            project="facilis",
        )
        self.assertEqual(test_model.slug, "omnis")
        self.assertEqual(test_model.dynamic_secret, "maiores")
        self.assertEqual(test_model.config, "inventore")
        self.assertEqual(test_model.project, "facilis")

    def test_revoke_lease_request_required_fields_missing(self):
        # Assert RevokeLeaseRequest class generation fails without required fields
        with self.assertRaises(TypeError):
            test_model = RevokeLeaseRequest()


if __name__ == "__main__":
    unittest.main()

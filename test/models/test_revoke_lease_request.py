import unittest
from src.dopplersdk.models.RevokeLeaseRequest import RevokeLeaseRequest


class TestRevokeLeaseRequestModel(unittest.TestCase):
    def test_true(self):
        self.assertTrue(True)

    def test_revoke_lease_request(self):
        # Create RevokeLeaseRequest class instance
        test_model = RevokeLeaseRequest(
            slug="architecto", dynamic_secret="iure", config="unde", project="et"
        )
        self.assertEqual(test_model.slug, "architecto")
        self.assertEqual(test_model.dynamic_secret, "iure")
        self.assertEqual(test_model.config, "unde")
        self.assertEqual(test_model.project, "et")

    def test_revoke_lease_request_required_fields_missing(self):
        # Assert RevokeLeaseRequest class generation fails without required fields
        with self.assertRaises(TypeError):
            test_model = RevokeLeaseRequest()


if __name__ == "__main__":
    unittest.main()

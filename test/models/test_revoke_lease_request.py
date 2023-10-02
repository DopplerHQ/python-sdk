import unittest
from src.dopplersdk.models.RevokeLeaseRequest import RevokeLeaseRequest


class TestRevokeLeaseRequestModel(unittest.TestCase):
    def test_true(self):
        self.assertTrue(True)

    def test_revoke_lease_request(self):
        # Create RevokeLeaseRequest class instance
        test_model = RevokeLeaseRequest(
            slug="cum", dynamic_secret="a", config="fuga", project="ratione"
        )
        self.assertEqual(test_model.slug, "cum")
        self.assertEqual(test_model.dynamic_secret, "a")
        self.assertEqual(test_model.config, "fuga")
        self.assertEqual(test_model.project, "ratione")

    def test_revoke_lease_request_required_fields_missing(self):
        # Assert RevokeLeaseRequest class generation fails without required fields
        with self.assertRaises(TypeError):
            test_model = RevokeLeaseRequest()


if __name__ == "__main__":
    unittest.main()

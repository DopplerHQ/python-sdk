import unittest
from src.dopplersdk.models.DynamicSecretsRevokeLeaseRequest import (
    DynamicSecretsRevokeLeaseRequest,
)


class TestDynamicSecretsRevokeLeaseRequestModel(unittest.TestCase):
    def test_true(self):
        self.assertTrue(True)

    def test_dynamic_secrets_revoke_lease_request(self):
        # Create DynamicSecretsRevokeLeaseRequest class instance
        test_model = DynamicSecretsRevokeLeaseRequest(
            slug="numquam", dynamic_secret="libero", config="nostrum", project="ad"
        )
        self.assertEqual(test_model.slug, "numquam")
        self.assertEqual(test_model.dynamic_secret, "libero")
        self.assertEqual(test_model.config, "nostrum")
        self.assertEqual(test_model.project, "ad")

    def test_dynamic_secrets_revoke_lease_request_required_fields_missing(self):
        # Assert DynamicSecretsRevokeLeaseRequest class generation fails without required fields
        with self.assertRaises(TypeError):
            test_model = DynamicSecretsRevokeLeaseRequest()


if __name__ == "__main__":
    unittest.main()

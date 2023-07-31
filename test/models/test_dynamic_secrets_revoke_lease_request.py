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
            slug="corrupti",
            dynamic_secret="cupiditate",
            config="dicta",
            project="doloremque",
        )
        self.assertEqual(test_model.slug, "corrupti")
        self.assertEqual(test_model.dynamic_secret, "cupiditate")
        self.assertEqual(test_model.config, "dicta")
        self.assertEqual(test_model.project, "doloremque")

    def test_dynamic_secrets_revoke_lease_request_required_fields_missing(self):
        # Assert DynamicSecretsRevokeLeaseRequest class generation fails without required fields
        with self.assertRaises(TypeError):
            test_model = DynamicSecretsRevokeLeaseRequest()


if __name__ == "__main__":
    unittest.main()

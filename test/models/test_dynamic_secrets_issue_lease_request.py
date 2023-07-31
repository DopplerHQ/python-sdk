import unittest
from src.dopplersdk.models.DynamicSecretsIssueLeaseRequest import (
    DynamicSecretsIssueLeaseRequest,
)


class TestDynamicSecretsIssueLeaseRequestModel(unittest.TestCase):
    def test_true(self):
        self.assertTrue(True)

    def test_dynamic_secrets_issue_lease_request(self):
        # Create DynamicSecretsIssueLeaseRequest class instance
        test_model = DynamicSecretsIssueLeaseRequest(
            ttl_sec=2, dynamic_secret="incidunt", config="eligendi", project="dolorum"
        )
        self.assertEqual(test_model.ttl_sec, 2)
        self.assertEqual(test_model.dynamic_secret, "incidunt")
        self.assertEqual(test_model.config, "eligendi")
        self.assertEqual(test_model.project, "dolorum")

    def test_dynamic_secrets_issue_lease_request_required_fields_missing(self):
        # Assert DynamicSecretsIssueLeaseRequest class generation fails without required fields
        with self.assertRaises(TypeError):
            test_model = DynamicSecretsIssueLeaseRequest()


if __name__ == "__main__":
    unittest.main()

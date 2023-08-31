import unittest
from src.dopplersdk.models.IssueLeaseRequest import IssueLeaseRequest


class TestIssueLeaseRequestModel(unittest.TestCase):
    def test_true(self):
        self.assertTrue(True)

    def test_issue_lease_request(self):
        # Create IssueLeaseRequest class instance
        test_model = IssueLeaseRequest(
            ttl_sec=6, dynamic_secret="sint", config="occaecati", project="perferendis"
        )
        self.assertEqual(test_model.ttl_sec, 6)
        self.assertEqual(test_model.dynamic_secret, "sint")
        self.assertEqual(test_model.config, "occaecati")
        self.assertEqual(test_model.project, "perferendis")

    def test_issue_lease_request_required_fields_missing(self):
        # Assert IssueLeaseRequest class generation fails without required fields
        with self.assertRaises(TypeError):
            test_model = IssueLeaseRequest()


if __name__ == "__main__":
    unittest.main()

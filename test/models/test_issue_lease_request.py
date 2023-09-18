import unittest
from src.dopplersdk.models.IssueLeaseRequest import IssueLeaseRequest


class TestIssueLeaseRequestModel(unittest.TestCase):
    def test_true(self):
        self.assertTrue(True)

    def test_issue_lease_request(self):
        # Create IssueLeaseRequest class instance
        test_model = IssueLeaseRequest(
            ttl_sec=7, dynamic_secret="nesciunt", config="labore", project="vero"
        )
        self.assertEqual(test_model.ttl_sec, 7)
        self.assertEqual(test_model.dynamic_secret, "nesciunt")
        self.assertEqual(test_model.config, "labore")
        self.assertEqual(test_model.project, "vero")

    def test_issue_lease_request_required_fields_missing(self):
        # Assert IssueLeaseRequest class generation fails without required fields
        with self.assertRaises(TypeError):
            test_model = IssueLeaseRequest()


if __name__ == "__main__":
    unittest.main()

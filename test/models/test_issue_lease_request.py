import unittest
from src.dopplersdk.models.IssueLeaseRequest import IssueLeaseRequest


class TestIssueLeaseRequestModel(unittest.TestCase):
    def test_true(self):
        self.assertTrue(True)

    def test_issue_lease_request(self):
        # Create IssueLeaseRequest class instance
        test_model = IssueLeaseRequest(
            ttl_sec=3, dynamic_secret="cumque", config="debitis", project="molestiae"
        )
        self.assertEqual(test_model.ttl_sec, 3)
        self.assertEqual(test_model.dynamic_secret, "cumque")
        self.assertEqual(test_model.config, "debitis")
        self.assertEqual(test_model.project, "molestiae")

    def test_issue_lease_request_required_fields_missing(self):
        # Assert IssueLeaseRequest class generation fails without required fields
        with self.assertRaises(TypeError):
            test_model = IssueLeaseRequest()


if __name__ == "__main__":
    unittest.main()

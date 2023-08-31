import unittest
from src.dopplersdk.models.IssueLeaseResponse import IssueLeaseResponse


class TestIssueLeaseResponseModel(unittest.TestCase):
    def test_true(self):
        self.assertTrue(True)

    def test_issue_lease_response(self):
        # Create IssueLeaseResponse class instance
        test_model = IssueLeaseResponse(
            success=True, id="quas", expires_at="qui", value={"illo": 8}
        )
        self.assertEqual(test_model.success, True)
        self.assertEqual(test_model.id, "quas")
        self.assertEqual(test_model.expires_at, "qui")
        self.assertEqual(test_model.value, {"illo": 8})


if __name__ == "__main__":
    unittest.main()

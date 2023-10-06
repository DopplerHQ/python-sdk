import unittest
from src.dopplersdk.models.IssueLeaseResponse import IssueLeaseResponse


class TestIssueLeaseResponseModel(unittest.TestCase):
    def test_true(self):
        self.assertTrue(True)

    def test_issue_lease_response(self):
        # Create IssueLeaseResponse class instance
        test_model = IssueLeaseResponse(
            success=True, id="sapiente", expires_at="impedit", value={"aliquid": 4}
        )
        self.assertEqual(test_model.success, True)
        self.assertEqual(test_model.id, "sapiente")
        self.assertEqual(test_model.expires_at, "impedit")
        self.assertEqual(test_model.value, {"aliquid": 4})


if __name__ == "__main__":
    unittest.main()

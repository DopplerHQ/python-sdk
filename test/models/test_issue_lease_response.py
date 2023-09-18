import unittest
from src.dopplersdk.models.IssueLeaseResponse import IssueLeaseResponse


class TestIssueLeaseResponseModel(unittest.TestCase):
    def test_true(self):
        self.assertTrue(True)

    def test_issue_lease_response(self):
        # Create IssueLeaseResponse class instance
        test_model = IssueLeaseResponse(
            success=True, id="earum", expires_at="libero", value={"ex": 1}
        )
        self.assertEqual(test_model.success, True)
        self.assertEqual(test_model.id, "earum")
        self.assertEqual(test_model.expires_at, "libero")
        self.assertEqual(test_model.value, {"ex": 1})


if __name__ == "__main__":
    unittest.main()

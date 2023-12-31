import unittest
from src.dopplersdk.models.IssueLeaseResponse import IssueLeaseResponse


class TestIssueLeaseResponseModel(unittest.TestCase):
    def test_true(self):
        self.assertTrue(True)

    def test_issue_lease_response(self):
        # Create IssueLeaseResponse class instance
        test_model = IssueLeaseResponse(
            success=True, id="harum", expires_at="molestiae", value={"deserunt": 4}
        )
        self.assertEqual(test_model.success, True)
        self.assertEqual(test_model.id, "harum")
        self.assertEqual(test_model.expires_at, "molestiae")
        self.assertEqual(test_model.value, {"deserunt": 4})


if __name__ == "__main__":
    unittest.main()

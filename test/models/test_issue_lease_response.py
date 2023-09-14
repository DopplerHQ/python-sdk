import unittest
from src.dopplersdk.models.IssueLeaseResponse import IssueLeaseResponse


class TestIssueLeaseResponseModel(unittest.TestCase):
    def test_true(self):
        self.assertTrue(True)

    def test_issue_lease_response(self):
        # Create IssueLeaseResponse class instance
        test_model = IssueLeaseResponse(
            success=True, id="similique", expires_at="cupiditate", value={"ullam": 1}
        )
        self.assertEqual(test_model.success, True)
        self.assertEqual(test_model.id, "similique")
        self.assertEqual(test_model.expires_at, "cupiditate")
        self.assertEqual(test_model.value, {"ullam": 1})


if __name__ == "__main__":
    unittest.main()

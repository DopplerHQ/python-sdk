import unittest
from src.dopplersdk.models.IssueLeaseResponse import IssueLeaseResponse


class TestIssueLeaseResponseModel(unittest.TestCase):
    def test_true(self):
        self.assertTrue(True)

    def test_issue_lease_response(self):
        # Create IssueLeaseResponse class instance
        test_model = IssueLeaseResponse(
            success=True, id="quis", expires_at="cumque", value={"eaque": 3}
        )
        self.assertEqual(test_model.success, True)
        self.assertEqual(test_model.id, "quis")
        self.assertEqual(test_model.expires_at, "cumque")
        self.assertEqual(test_model.value, {"eaque": 3})


if __name__ == "__main__":
    unittest.main()

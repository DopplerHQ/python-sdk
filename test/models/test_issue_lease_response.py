import unittest
from src.dopplersdk.models.IssueLeaseResponse import IssueLeaseResponse


class TestIssueLeaseResponseModel(unittest.TestCase):
    def test_true(self):
        self.assertTrue(True)

    def test_issue_lease_response(self):
        # Create IssueLeaseResponse class instance
        test_model = IssueLeaseResponse(
            success=True, id="porro", expires_at="possimus", value={"iusto": 6}
        )
        self.assertEqual(test_model.success, True)
        self.assertEqual(test_model.id, "porro")
        self.assertEqual(test_model.expires_at, "possimus")
        self.assertEqual(test_model.value, {"iusto": 6})


if __name__ == "__main__":
    unittest.main()

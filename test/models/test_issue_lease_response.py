import unittest
from src.dopplersdk.models.IssueLeaseResponse import IssueLeaseResponse


class TestIssueLeaseResponseModel(unittest.TestCase):
    def test_true(self):
        self.assertTrue(True)

    def test_issue_lease_response(self):
        # Create IssueLeaseResponse class instance
        test_model = IssueLeaseResponse(
            success=True, id="alias", expires_at="eveniet", value={"illum": 7}
        )
        self.assertEqual(test_model.success, True)
        self.assertEqual(test_model.id, "alias")
        self.assertEqual(test_model.expires_at, "eveniet")
        self.assertEqual(test_model.value, {"illum": 7})


if __name__ == "__main__":
    unittest.main()

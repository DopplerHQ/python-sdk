import unittest
from src.dopplersdk.models.IssueLeaseResponse import IssueLeaseResponse


class TestIssueLeaseResponseModel(unittest.TestCase):
    def test_true(self):
        self.assertTrue(True)

    def test_issue_lease_response(self):
        # Create IssueLeaseResponse class instance
        test_model = IssueLeaseResponse(
            success=True, id="esse", expires_at="ad", value={"nulla": 9}
        )
        self.assertEqual(test_model.success, True)
        self.assertEqual(test_model.id, "esse")
        self.assertEqual(test_model.expires_at, "ad")
        self.assertEqual(test_model.value, {"nulla": 9})


if __name__ == "__main__":
    unittest.main()

import unittest
from src.dopplersdk.models.IssueLeaseResponse import IssueLeaseResponse


class TestIssueLeaseResponseModel(unittest.TestCase):
    def test_true(self):
        self.assertTrue(True)

    def test_issue_lease_response(self):
        # Create IssueLeaseResponse class instance
        test_model = IssueLeaseResponse(
            success=True, id="magni", expires_at="cum", value={"nemo": 1}
        )
        self.assertEqual(test_model.success, True)
        self.assertEqual(test_model.id, "magni")
        self.assertEqual(test_model.expires_at, "cum")
        self.assertEqual(test_model.value, {"nemo": 1})


if __name__ == "__main__":
    unittest.main()

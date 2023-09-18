import unittest
from src.dopplersdk.models.ProjectMembersUpdateRequest import (
    ProjectMembersUpdateRequest,
)


class TestProjectMembersUpdateRequestModel(unittest.TestCase):
    def test_true(self):
        self.assertTrue(True)

    def test_project_members_update_request(self):
        # Create ProjectMembersUpdateRequest class instance
        test_model = ProjectMembersUpdateRequest(
            role="soluta", environments=["ipsam", "veritatis"]
        )
        self.assertEqual(test_model.role, "soluta")
        self.assertEqual(test_model.environments, ["ipsam", "veritatis"])


if __name__ == "__main__":
    unittest.main()

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
            role="fugiat", environments=["qui", "qui"]
        )
        self.assertEqual(test_model.role, "fugiat")
        self.assertEqual(test_model.environments, ["qui", "qui"])


if __name__ == "__main__":
    unittest.main()

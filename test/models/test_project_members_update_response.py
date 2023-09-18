import unittest
from src.dopplersdk.models.ProjectMembersUpdateResponse import (
    ProjectMembersUpdateResponse,
)


class TestProjectMembersUpdateResponseModel(unittest.TestCase):
    def test_true(self):
        self.assertTrue(True)

    def test_project_members_update_response(self):
        # Create ProjectMembersUpdateResponse class instance
        test_model = ProjectMembersUpdateResponse(member={"ullam": 4})
        self.assertEqual(test_model.member, {"ullam": 4})


if __name__ == "__main__":
    unittest.main()

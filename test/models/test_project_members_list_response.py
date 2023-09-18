import unittest
from src.dopplersdk.models.ProjectMembersListResponse import ProjectMembersListResponse


class TestProjectMembersListResponseModel(unittest.TestCase):
    def test_true(self):
        self.assertTrue(True)

    def test_project_members_list_response(self):
        # Create ProjectMembersListResponse class instance
        test_model = ProjectMembersListResponse(members=["repudiandae", "corrupti"])
        self.assertEqual(test_model.members, ["repudiandae", "corrupti"])


if __name__ == "__main__":
    unittest.main()

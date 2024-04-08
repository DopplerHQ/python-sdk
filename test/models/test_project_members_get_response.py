import unittest
from src.dopplersdk.models.ProjectMembersGetResponse import ProjectMembersGetResponse


class TestProjectMembersGetResponseModel(unittest.TestCase):
    def test_true(self):
        self.assertTrue(True)

    def test_project_members_get_response(self):
        # Create ProjectMembersGetResponse class instance
        test_model = ProjectMembersGetResponse(member={"iste": 5})
        self.assertEqual(test_model.member, {"iste": 5})


if __name__ == "__main__":
    unittest.main()

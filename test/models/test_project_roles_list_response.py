import unittest
from src.dopplersdk.models.ProjectRolesListResponse import ProjectRolesListResponse


class TestProjectRolesListResponseModel(unittest.TestCase):
    def test_true(self):
        self.assertTrue(True)

    def test_project_roles_list_response(self):
        # Create ProjectRolesListResponse class instance
        test_model = ProjectRolesListResponse(roles=["possimus", "architecto"])
        self.assertEqual(test_model.roles, ["possimus", "architecto"])


if __name__ == "__main__":
    unittest.main()

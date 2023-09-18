import unittest
from src.dopplersdk.models.ProjectRolesUpdateResponse import ProjectRolesUpdateResponse


class TestProjectRolesUpdateResponseModel(unittest.TestCase):
    def test_true(self):
        self.assertTrue(True)

    def test_project_roles_update_response(self):
        # Create ProjectRolesUpdateResponse class instance
        test_model = ProjectRolesUpdateResponse(role={"soluta": 8})
        self.assertEqual(test_model.role, {"soluta": 8})


if __name__ == "__main__":
    unittest.main()

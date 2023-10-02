import unittest
from src.dopplersdk.models.ProjectRolesUpdateResponse import ProjectRolesUpdateResponse


class TestProjectRolesUpdateResponseModel(unittest.TestCase):
    def test_true(self):
        self.assertTrue(True)

    def test_project_roles_update_response(self):
        # Create ProjectRolesUpdateResponse class instance
        test_model = ProjectRolesUpdateResponse(role={"quidem": 5})
        self.assertEqual(test_model.role, {"quidem": 5})


if __name__ == "__main__":
    unittest.main()

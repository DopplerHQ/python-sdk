import unittest
from src.dopplersdk.models.ProjectRolesGetResponse import ProjectRolesGetResponse


class TestProjectRolesGetResponseModel(unittest.TestCase):
    def test_true(self):
        self.assertTrue(True)

    def test_project_roles_get_response(self):
        # Create ProjectRolesGetResponse class instance
        test_model = ProjectRolesGetResponse(role={"expedita": 6})
        self.assertEqual(test_model.role, {"expedita": 6})


if __name__ == "__main__":
    unittest.main()

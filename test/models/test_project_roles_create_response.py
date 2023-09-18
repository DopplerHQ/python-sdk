import unittest
from src.dopplersdk.models.ProjectRolesCreateResponse import ProjectRolesCreateResponse


class TestProjectRolesCreateResponseModel(unittest.TestCase):
    def test_true(self):
        self.assertTrue(True)

    def test_project_roles_create_response(self):
        # Create ProjectRolesCreateResponse class instance
        test_model = ProjectRolesCreateResponse(role={"odio": 6})
        self.assertEqual(test_model.role, {"odio": 6})


if __name__ == "__main__":
    unittest.main()

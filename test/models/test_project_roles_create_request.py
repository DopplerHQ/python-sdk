import unittest
from src.dopplersdk.models.ProjectRolesCreateRequest import ProjectRolesCreateRequest


class TestProjectRolesCreateRequestModel(unittest.TestCase):
    def test_true(self):
        self.assertTrue(True)

    def test_project_roles_create_request(self):
        # Create ProjectRolesCreateRequest class instance
        test_model = ProjectRolesCreateRequest(
            permissions=["architecto", "omnis"], name="cum"
        )
        self.assertEqual(test_model.permissions, ["architecto", "omnis"])
        self.assertEqual(test_model.name, "cum")

    def test_project_roles_create_request_required_fields_missing(self):
        # Assert ProjectRolesCreateRequest class generation fails without required fields
        with self.assertRaises(TypeError):
            test_model = ProjectRolesCreateRequest()


if __name__ == "__main__":
    unittest.main()

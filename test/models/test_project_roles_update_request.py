import unittest
from src.dopplersdk.models.ProjectRolesUpdateRequest import ProjectRolesUpdateRequest


class TestProjectRolesUpdateRequestModel(unittest.TestCase):
    def test_true(self):
        self.assertTrue(True)

    def test_project_roles_update_request(self):
        # Create ProjectRolesUpdateRequest class instance
        test_model = ProjectRolesUpdateRequest(
            name="odio", permissions=["voluptatibus", "quia"]
        )
        self.assertEqual(test_model.name, "odio")
        self.assertEqual(test_model.permissions, ["voluptatibus", "quia"])


if __name__ == "__main__":
    unittest.main()

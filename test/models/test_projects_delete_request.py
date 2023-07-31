import unittest
from src.dopplersdk.models.ProjectsDeleteRequest import ProjectsDeleteRequest


class TestProjectsDeleteRequestModel(unittest.TestCase):
    def test_true(self):
        self.assertTrue(True)

    def test_projects_delete_request(self):
        # Create ProjectsDeleteRequest class instance
        test_model = ProjectsDeleteRequest(project="a")
        self.assertEqual(test_model.project, "a")

    def test_projects_delete_request_required_fields_missing(self):
        # Assert ProjectsDeleteRequest class generation fails without required fields
        with self.assertRaises(TypeError):
            test_model = ProjectsDeleteRequest()


if __name__ == "__main__":
    unittest.main()

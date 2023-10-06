import unittest
from src.dopplersdk.models.ProjectsGetResponse import ProjectsGetResponse


class TestProjectsGetResponseModel(unittest.TestCase):
    def test_true(self):
        self.assertTrue(True)

    def test_projects_get_response(self):
        # Create ProjectsGetResponse class instance
        test_model = ProjectsGetResponse(project={"quod": 2})
        self.assertEqual(test_model.project, {"quod": 2})


if __name__ == "__main__":
    unittest.main()

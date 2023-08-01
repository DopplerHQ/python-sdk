import unittest
from src.dopplersdk.models.ProjectsGet200Response import ProjectsGet200Response


class TestProjectsGet200ResponseModel(unittest.TestCase):
    def test_true(self):
        self.assertTrue(True)

    def test_projects_get200_response(self):
        # Create ProjectsGet200Response class instance
        test_model = ProjectsGet200Response(project={"tempore": 6})
        self.assertEqual(test_model.project, {"tempore": 6})


if __name__ == "__main__":
    unittest.main()

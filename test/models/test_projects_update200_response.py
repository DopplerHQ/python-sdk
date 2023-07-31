import unittest
from src.dopplersdk.models.ProjectsUpdate200Response import ProjectsUpdate200Response


class TestProjectsUpdate200ResponseModel(unittest.TestCase):
    def test_true(self):
        self.assertTrue(True)

    def test_projects_update200_response(self):
        # Create ProjectsUpdate200Response class instance
        test_model = ProjectsUpdate200Response(project={"neque": 3})
        self.assertEqual(test_model.project, {"neque": 3})


if __name__ == "__main__":
    unittest.main()

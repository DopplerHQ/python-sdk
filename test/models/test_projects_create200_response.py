import unittest
from src.dopplersdk.models.ProjectsCreate200Response import ProjectsCreate200Response


class TestProjectsCreate200ResponseModel(unittest.TestCase):
    def test_true(self):
        self.assertTrue(True)

    def test_projects_create200_response(self):
        # Create ProjectsCreate200Response class instance
        test_model = ProjectsCreate200Response(project={"corrupti": 2})
        self.assertEqual(test_model.project, {"corrupti": 2})


if __name__ == "__main__":
    unittest.main()
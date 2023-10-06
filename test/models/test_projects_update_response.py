import unittest
from src.dopplersdk.models.ProjectsUpdateResponse import ProjectsUpdateResponse


class TestProjectsUpdateResponseModel(unittest.TestCase):
    def test_true(self):
        self.assertTrue(True)

    def test_projects_update_response(self):
        # Create ProjectsUpdateResponse class instance
        test_model = ProjectsUpdateResponse(project={"laborum": 2})
        self.assertEqual(test_model.project, {"laborum": 2})


if __name__ == "__main__":
    unittest.main()

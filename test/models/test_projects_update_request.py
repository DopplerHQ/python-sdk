import unittest
from src.dopplersdk.models.ProjectsUpdateRequest import ProjectsUpdateRequest


class TestProjectsUpdateRequestModel(unittest.TestCase):
    def test_true(self):
        self.assertTrue(True)

    def test_projects_update_request(self):
        # Create ProjectsUpdateRequest class instance
        test_model = ProjectsUpdateRequest(
            name="at", project="nostrum", description="suscipit"
        )
        self.assertEqual(test_model.name, "at")
        self.assertEqual(test_model.project, "nostrum")
        self.assertEqual(test_model.description, "suscipit")

    def test_projects_update_request_required_fields_missing(self):
        # Assert ProjectsUpdateRequest class generation fails without required fields
        with self.assertRaises(TypeError):
            test_model = ProjectsUpdateRequest()


if __name__ == "__main__":
    unittest.main()

import unittest
from src.dopplersdk.models.ProjectsCreateRequest import ProjectsCreateRequest


class TestProjectsCreateRequestModel(unittest.TestCase):
    def test_true(self):
        self.assertTrue(True)

    def test_projects_create_request(self):
        # Create ProjectsCreateRequest class instance
        test_model = ProjectsCreateRequest(name="expedita", description="temporibus")
        self.assertEqual(test_model.name, "expedita")
        self.assertEqual(test_model.description, "temporibus")

    def test_projects_create_request_required_fields_missing(self):
        # Assert ProjectsCreateRequest class generation fails without required fields
        with self.assertRaises(TypeError):
            test_model = ProjectsCreateRequest()


if __name__ == "__main__":
    unittest.main()

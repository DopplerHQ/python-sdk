import unittest
from src.dopplersdk.models.CloneRequest import CloneRequest


class TestCloneRequestModel(unittest.TestCase):
    def test_true(self):
        self.assertTrue(True)

    def test_clone_request(self):
        # Create CloneRequest class instance
        test_model = CloneRequest(name="quidem", config="incidunt", project="beatae")
        self.assertEqual(test_model.name, "quidem")
        self.assertEqual(test_model.config, "incidunt")
        self.assertEqual(test_model.project, "beatae")

    def test_clone_request_required_fields_missing(self):
        # Assert CloneRequest class generation fails without required fields
        with self.assertRaises(TypeError):
            test_model = CloneRequest()


if __name__ == "__main__":
    unittest.main()

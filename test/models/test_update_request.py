import unittest
from src.dopplersdk.models.UpdateRequest import UpdateRequest


class TestUpdateRequestModel(unittest.TestCase):
    def test_true(self):
        self.assertTrue(True)

    def test_update_request(self):
        # Create UpdateRequest class instance
        test_model = UpdateRequest(
            name="autem", project="incidunt", description="similique"
        )
        self.assertEqual(test_model.name, "autem")
        self.assertEqual(test_model.project, "incidunt")
        self.assertEqual(test_model.description, "similique")

    def test_update_request_required_fields_missing(self):
        # Assert UpdateRequest class generation fails without required fields
        with self.assertRaises(TypeError):
            test_model = UpdateRequest()


if __name__ == "__main__":
    unittest.main()

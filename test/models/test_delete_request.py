import unittest
from src.dopplersdk.models.DeleteRequest import DeleteRequest


class TestDeleteRequestModel(unittest.TestCase):
    def test_true(self):
        self.assertTrue(True)

    def test_delete_request(self):
        # Create DeleteRequest class instance
        test_model = DeleteRequest(project="magnam")
        self.assertEqual(test_model.project, "magnam")

    def test_delete_request_required_fields_missing(self):
        # Assert DeleteRequest class generation fails without required fields
        with self.assertRaises(TypeError):
            test_model = DeleteRequest()


if __name__ == "__main__":
    unittest.main()

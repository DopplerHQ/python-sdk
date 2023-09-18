import unittest
from src.dopplersdk.models.UpdateRequest import UpdateRequest


class TestUpdateRequestModel(unittest.TestCase):
    def test_true(self):
        self.assertTrue(True)

    def test_update_request(self):
        # Create UpdateRequest class instance
        test_model = UpdateRequest(
            secrets={"reiciendis": 1}, config="architecto", project="adipisci"
        )
        self.assertEqual(test_model.secrets, {"reiciendis": 1})
        self.assertEqual(test_model.config, "architecto")
        self.assertEqual(test_model.project, "adipisci")

    def test_update_request_required_fields_missing(self):
        # Assert UpdateRequest class generation fails without required fields
        with self.assertRaises(TypeError):
            test_model = UpdateRequest()


if __name__ == "__main__":
    unittest.main()

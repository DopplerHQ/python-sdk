import unittest
from src.dopplersdk.models.UpdateNoteRequest import UpdateNoteRequest


class TestUpdateNoteRequestModel(unittest.TestCase):
    def test_true(self):
        self.assertTrue(True)

    def test_update_note_request(self):
        # Create UpdateNoteRequest class instance
        test_model = UpdateNoteRequest(
            note="quae", secret="animi", config="amet", project="quaerat"
        )
        self.assertEqual(test_model.note, "quae")
        self.assertEqual(test_model.secret, "animi")
        self.assertEqual(test_model.config, "amet")
        self.assertEqual(test_model.project, "quaerat")

    def test_update_note_request_required_fields_missing(self):
        # Assert UpdateNoteRequest class generation fails without required fields
        with self.assertRaises(TypeError):
            test_model = UpdateNoteRequest()


if __name__ == "__main__":
    unittest.main()

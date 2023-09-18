import unittest
from src.dopplersdk.models.UpdateNoteRequest import UpdateNoteRequest


class TestUpdateNoteRequestModel(unittest.TestCase):
    def test_true(self):
        self.assertTrue(True)

    def test_update_note_request(self):
        # Create UpdateNoteRequest class instance
        test_model = UpdateNoteRequest(
            note="earum", secret="numquam", config="autem", project="aspernatur"
        )
        self.assertEqual(test_model.note, "earum")
        self.assertEqual(test_model.secret, "numquam")
        self.assertEqual(test_model.config, "autem")
        self.assertEqual(test_model.project, "aspernatur")

    def test_update_note_request_required_fields_missing(self):
        # Assert UpdateNoteRequest class generation fails without required fields
        with self.assertRaises(TypeError):
            test_model = UpdateNoteRequest()


if __name__ == "__main__":
    unittest.main()

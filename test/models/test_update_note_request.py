import unittest
from src.dopplersdk.models.UpdateNoteRequest import UpdateNoteRequest


class TestUpdateNoteRequestModel(unittest.TestCase):
    def test_true(self):
        self.assertTrue(True)

    def test_update_note_request(self):
        # Create UpdateNoteRequest class instance
        test_model = UpdateNoteRequest(
            note="expedita", secret="expedita", config="iusto", project="iste"
        )
        self.assertEqual(test_model.note, "expedita")
        self.assertEqual(test_model.secret, "expedita")
        self.assertEqual(test_model.config, "iusto")
        self.assertEqual(test_model.project, "iste")

    def test_update_note_request_required_fields_missing(self):
        # Assert UpdateNoteRequest class generation fails without required fields
        with self.assertRaises(TypeError):
            test_model = UpdateNoteRequest()


if __name__ == "__main__":
    unittest.main()

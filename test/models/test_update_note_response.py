import unittest
from src.dopplersdk.models.UpdateNoteResponse import UpdateNoteResponse


class TestUpdateNoteResponseModel(unittest.TestCase):
    def test_true(self):
        self.assertTrue(True)

    def test_update_note_response(self):
        # Create UpdateNoteResponse class instance
        test_model = UpdateNoteResponse(secret="illum", note="error")
        self.assertEqual(test_model.secret, "illum")
        self.assertEqual(test_model.note, "error")


if __name__ == "__main__":
    unittest.main()

import unittest
from src.dopplersdk.models.UpdateNoteResponse import UpdateNoteResponse


class TestUpdateNoteResponseModel(unittest.TestCase):
    def test_true(self):
        self.assertTrue(True)

    def test_update_note_response(self):
        # Create UpdateNoteResponse class instance
        test_model = UpdateNoteResponse(secret="veniam", note="hic")
        self.assertEqual(test_model.secret, "veniam")
        self.assertEqual(test_model.note, "hic")


if __name__ == "__main__":
    unittest.main()

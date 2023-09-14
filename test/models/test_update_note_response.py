import unittest
from src.dopplersdk.models.UpdateNoteResponse import UpdateNoteResponse


class TestUpdateNoteResponseModel(unittest.TestCase):
    def test_true(self):
        self.assertTrue(True)

    def test_update_note_response(self):
        # Create UpdateNoteResponse class instance
        test_model = UpdateNoteResponse(secret="placeat", note="aliquid")
        self.assertEqual(test_model.secret, "placeat")
        self.assertEqual(test_model.note, "aliquid")


if __name__ == "__main__":
    unittest.main()

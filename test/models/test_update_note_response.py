import unittest
from src.dopplersdk.models.UpdateNoteResponse import UpdateNoteResponse


class TestUpdateNoteResponseModel(unittest.TestCase):
    def test_true(self):
        self.assertTrue(True)

    def test_update_note_response(self):
        # Create UpdateNoteResponse class instance
        test_model = UpdateNoteResponse(secret="reprehenderit", note="iste")
        self.assertEqual(test_model.secret, "reprehenderit")
        self.assertEqual(test_model.note, "iste")


if __name__ == "__main__":
    unittest.main()

import unittest
from src.dopplersdk.models.SecretsUpdateNoteRequest import SecretsUpdateNoteRequest


class TestSecretsUpdateNoteRequestModel(unittest.TestCase):
    def test_true(self):
        self.assertTrue(True)

    def test_secrets_update_note_request(self):
        # Create SecretsUpdateNoteRequest class instance
        test_model = SecretsUpdateNoteRequest(
            note="suscipit", secret="in", config="consectetur", project="soluta"
        )
        self.assertEqual(test_model.note, "suscipit")
        self.assertEqual(test_model.secret, "in")
        self.assertEqual(test_model.config, "consectetur")
        self.assertEqual(test_model.project, "soluta")

    def test_secrets_update_note_request_required_fields_missing(self):
        # Assert SecretsUpdateNoteRequest class generation fails without required fields
        with self.assertRaises(TypeError):
            test_model = SecretsUpdateNoteRequest()


if __name__ == "__main__":
    unittest.main()

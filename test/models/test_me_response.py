import unittest
from src.dopplersdk.models.MeResponse import MeResponse


class TestMeResponseModel(unittest.TestCase):
    def test_true(self):
        self.assertTrue(True)

    def test_me_response(self):
        # Create MeResponse class instance
        test_model = MeResponse(
            slug="recusandae",
            name="dolorem",
            created_at="esse",
            last_seen_at="nisi",
            token_preview="iusto",
            workplace={"quam": 4},
            type_="quibusdam",
        )
        self.assertEqual(test_model.slug, "recusandae")
        self.assertEqual(test_model.name, "dolorem")
        self.assertEqual(test_model.created_at, "esse")
        self.assertEqual(test_model.last_seen_at, "nisi")
        self.assertEqual(test_model.token_preview, "iusto")
        self.assertEqual(test_model.workplace, {"quam": 4})
        self.assertEqual(test_model.type_, "quibusdam")


if __name__ == "__main__":
    unittest.main()

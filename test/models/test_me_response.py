import unittest
from src.dopplersdk.models.MeResponse import MeResponse


class TestMeResponseModel(unittest.TestCase):
    def test_true(self):
        self.assertTrue(True)

    def test_me_response(self):
        # Create MeResponse class instance
        test_model = MeResponse(
            slug="ullam",
            name="eos",
            created_at="recusandae",
            last_seen_at="iusto",
            token_preview="commodi",
            workplace={"aut": 8},
            type_="illum",
        )
        self.assertEqual(test_model.slug, "ullam")
        self.assertEqual(test_model.name, "eos")
        self.assertEqual(test_model.created_at, "recusandae")
        self.assertEqual(test_model.last_seen_at, "iusto")
        self.assertEqual(test_model.token_preview, "commodi")
        self.assertEqual(test_model.workplace, {"aut": 8})
        self.assertEqual(test_model.type_, "illum")


if __name__ == "__main__":
    unittest.main()

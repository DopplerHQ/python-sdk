import unittest
from src.dopplersdk.models.MeResponse import MeResponse


class TestMeResponseModel(unittest.TestCase):
    def test_true(self):
        self.assertTrue(True)

    def test_me_response(self):
        # Create MeResponse class instance
        test_model = MeResponse(
            slug="exercitationem",
            name="recusandae",
            created_at="porro",
            last_seen_at="quidem",
            token_preview="quae",
            workplace={"ducimus": 1},
            type_="earum",
        )
        self.assertEqual(test_model.slug, "exercitationem")
        self.assertEqual(test_model.name, "recusandae")
        self.assertEqual(test_model.created_at, "porro")
        self.assertEqual(test_model.last_seen_at, "quidem")
        self.assertEqual(test_model.token_preview, "quae")
        self.assertEqual(test_model.workplace, {"ducimus": 1})
        self.assertEqual(test_model.type_, "earum")


if __name__ == "__main__":
    unittest.main()

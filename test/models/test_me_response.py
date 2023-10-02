import unittest
from src.dopplersdk.models.MeResponse import MeResponse


class TestMeResponseModel(unittest.TestCase):
    def test_true(self):
        self.assertTrue(True)

    def test_me_response(self):
        # Create MeResponse class instance
        test_model = MeResponse(
            slug="reprehenderit",
            name="temporibus",
            created_at="blanditiis",
            last_seen_at="laudantium",
            token_preview="consectetur",
            workplace={"autem": 3},
            type_="officia",
        )
        self.assertEqual(test_model.slug, "reprehenderit")
        self.assertEqual(test_model.name, "temporibus")
        self.assertEqual(test_model.created_at, "blanditiis")
        self.assertEqual(test_model.last_seen_at, "laudantium")
        self.assertEqual(test_model.token_preview, "consectetur")
        self.assertEqual(test_model.workplace, {"autem": 3})
        self.assertEqual(test_model.type_, "officia")


if __name__ == "__main__":
    unittest.main()

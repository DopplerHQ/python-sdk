import unittest
from src.dopplersdk.models.MeResponse import MeResponse


class TestMeResponseModel(unittest.TestCase):
    def test_true(self):
        self.assertTrue(True)

    def test_me_response(self):
        # Create MeResponse class instance
        test_model = MeResponse(
            slug="ex",
            name="dignissimos",
            created_at="veritatis",
            last_seen_at="temporibus",
            token_preview="commodi",
            workplace={"ipsam": 1},
            type_="veniam",
        )
        self.assertEqual(test_model.slug, "ex")
        self.assertEqual(test_model.name, "dignissimos")
        self.assertEqual(test_model.created_at, "veritatis")
        self.assertEqual(test_model.last_seen_at, "temporibus")
        self.assertEqual(test_model.token_preview, "commodi")
        self.assertEqual(test_model.workplace, {"ipsam": 1})
        self.assertEqual(test_model.type_, "veniam")


if __name__ == "__main__":
    unittest.main()

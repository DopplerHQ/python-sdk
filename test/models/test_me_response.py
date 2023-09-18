import unittest
from src.dopplersdk.models.MeResponse import MeResponse


class TestMeResponseModel(unittest.TestCase):
    def test_true(self):
        self.assertTrue(True)

    def test_me_response(self):
        # Create MeResponse class instance
        test_model = MeResponse(
            slug="veritatis",
            name="dolores",
            created_at="est",
            last_seen_at="ipsa",
            token_preview="minus",
            workplace={"sunt": 4},
            type_="perferendis",
        )
        self.assertEqual(test_model.slug, "veritatis")
        self.assertEqual(test_model.name, "dolores")
        self.assertEqual(test_model.created_at, "est")
        self.assertEqual(test_model.last_seen_at, "ipsa")
        self.assertEqual(test_model.token_preview, "minus")
        self.assertEqual(test_model.workplace, {"sunt": 4})
        self.assertEqual(test_model.type_, "perferendis")


if __name__ == "__main__":
    unittest.main()

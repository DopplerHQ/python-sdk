import unittest
from src.dopplersdk.models.MeResponse import MeResponse


class TestMeResponseModel(unittest.TestCase):
    def test_true(self):
        self.assertTrue(True)

    def test_me_response(self):
        # Create MeResponse class instance
        test_model = MeResponse(
            slug="nulla",
            name="ipsam",
            created_at="veritatis",
            last_seen_at="explicabo",
            token_preview="explicabo",
            workplace={"repellat": 8},
            type_="praesentium",
        )
        self.assertEqual(test_model.slug, "nulla")
        self.assertEqual(test_model.name, "ipsam")
        self.assertEqual(test_model.created_at, "veritatis")
        self.assertEqual(test_model.last_seen_at, "explicabo")
        self.assertEqual(test_model.token_preview, "explicabo")
        self.assertEqual(test_model.workplace, {"repellat": 8})
        self.assertEqual(test_model.type_, "praesentium")


if __name__ == "__main__":
    unittest.main()

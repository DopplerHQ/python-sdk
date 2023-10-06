import unittest
from src.dopplersdk.models.MeResponse import MeResponse


class TestMeResponseModel(unittest.TestCase):
    def test_true(self):
        self.assertTrue(True)

    def test_me_response(self):
        # Create MeResponse class instance
        test_model = MeResponse(
            slug="cupiditate",
            name="rem",
            created_at="expedita",
            last_seen_at="repudiandae",
            token_preview="voluptatum",
            workplace={"officia": 8},
            type_="enim",
        )
        self.assertEqual(test_model.slug, "cupiditate")
        self.assertEqual(test_model.name, "rem")
        self.assertEqual(test_model.created_at, "expedita")
        self.assertEqual(test_model.last_seen_at, "repudiandae")
        self.assertEqual(test_model.token_preview, "voluptatum")
        self.assertEqual(test_model.workplace, {"officia": 8})
        self.assertEqual(test_model.type_, "enim")


if __name__ == "__main__":
    unittest.main()

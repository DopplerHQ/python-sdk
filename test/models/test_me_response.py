import unittest
from src.dopplersdk.models.MeResponse import MeResponse


class TestMeResponseModel(unittest.TestCase):
    def test_true(self):
        self.assertTrue(True)

    def test_me_response(self):
        # Create MeResponse class instance
        test_model = MeResponse(
            slug="tempore",
            name="rem",
            created_at="nobis",
            last_seen_at="nemo",
            token_preview="iste",
            workplace={"at": 9},
            type_="alias",
        )
        self.assertEqual(test_model.slug, "tempore")
        self.assertEqual(test_model.name, "rem")
        self.assertEqual(test_model.created_at, "nobis")
        self.assertEqual(test_model.last_seen_at, "nemo")
        self.assertEqual(test_model.token_preview, "iste")
        self.assertEqual(test_model.workplace, {"at": 9})
        self.assertEqual(test_model.type_, "alias")


if __name__ == "__main__":
    unittest.main()

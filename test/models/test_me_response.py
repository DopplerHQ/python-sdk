import unittest
from src.dopplersdk.models.MeResponse import MeResponse


class TestMeResponseModel(unittest.TestCase):
    def test_true(self):
        self.assertTrue(True)

    def test_me_response(self):
        # Create MeResponse class instance
        test_model = MeResponse(
            slug="cupiditate",
            name="excepturi",
            created_at="doloribus",
            last_seen_at="cupiditate",
            token_preview="dolores",
            workplace={"culpa": 4},
            type_="aspernatur",
        )
        self.assertEqual(test_model.slug, "cupiditate")
        self.assertEqual(test_model.name, "excepturi")
        self.assertEqual(test_model.created_at, "doloribus")
        self.assertEqual(test_model.last_seen_at, "cupiditate")
        self.assertEqual(test_model.token_preview, "dolores")
        self.assertEqual(test_model.workplace, {"culpa": 4})
        self.assertEqual(test_model.type_, "aspernatur")


if __name__ == "__main__":
    unittest.main()

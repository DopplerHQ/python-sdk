import unittest
from src.dopplersdk.models.V3Me200Response import V3Me200Response


class TestV3Me200ResponseModel(unittest.TestCase):
    def test_true(self):
        self.assertTrue(True)

    def test_v_3_me200_response(self):
        # Create V3Me200Response class instance
        test_model = V3Me200Response(
            slug="quia",
            name="accusamus",
            created_at="debitis",
            last_seen_at="nam",
            type_="eveniet",
            token_preview="at",
            workplace={"eum": 8},
        )
        self.assertEqual(test_model.slug, "quia")
        self.assertEqual(test_model.name, "accusamus")
        self.assertEqual(test_model.created_at, "debitis")
        self.assertEqual(test_model.last_seen_at, "nam")
        self.assertEqual(test_model.type_, "eveniet")
        self.assertEqual(test_model.token_preview, "at")
        self.assertEqual(test_model.workplace, {"eum": 8})


if __name__ == "__main__":
    unittest.main()

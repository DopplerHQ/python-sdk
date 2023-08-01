import unittest
from src.dopplersdk.models.V3Me200Response import V3Me200Response


class TestV3Me200ResponseModel(unittest.TestCase):
    def test_true(self):
        self.assertTrue(True)

    def test_v_3_me200_response(self):
        # Create V3Me200Response class instance
        test_model = V3Me200Response(
            slug="libero",
            name="occaecati",
            created_at="voluptas",
            last_seen_at="fugit",
            type_="reiciendis",
            token_preview="dolorem",
            workplace={"commodi": 8},
        )
        self.assertEqual(test_model.slug, "libero")
        self.assertEqual(test_model.name, "occaecati")
        self.assertEqual(test_model.created_at, "voluptas")
        self.assertEqual(test_model.last_seen_at, "fugit")
        self.assertEqual(test_model.type_, "reiciendis")
        self.assertEqual(test_model.token_preview, "dolorem")
        self.assertEqual(test_model.workplace, {"commodi": 8})


if __name__ == "__main__":
    unittest.main()

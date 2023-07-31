import unittest
from src.dopplersdk.models.V3Me200Response import V3Me200Response


class TestV3Me200ResponseModel(unittest.TestCase):
    def test_true(self):
        self.assertTrue(True)

    def test_v_3_me200_response(self):
        # Create V3Me200Response class instance
        test_model = V3Me200Response(
            slug="incidunt",
            name="quis",
            created_at="corrupti",
            last_seen_at="assumenda",
            type_="earum",
            token_preview="a",
            workplace={"similique": 5},
        )
        self.assertEqual(test_model.slug, "incidunt")
        self.assertEqual(test_model.name, "quis")
        self.assertEqual(test_model.created_at, "corrupti")
        self.assertEqual(test_model.last_seen_at, "assumenda")
        self.assertEqual(test_model.type_, "earum")
        self.assertEqual(test_model.token_preview, "a")
        self.assertEqual(test_model.workplace, {"similique": 5})


if __name__ == "__main__":
    unittest.main()

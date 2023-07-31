import unittest
from src.dopplersdk.models.V3Me200Response import V3Me200Response


class TestV3Me200ResponseModel(unittest.TestCase):
    def test_true(self):
        self.assertTrue(True)

    def test_v_3_me200_response(self):
        # Create V3Me200Response class instance
        test_model = V3Me200Response(
            slug="laborum",
            name="beatae",
            created_at="reprehenderit",
            last_seen_at="voluptatibus",
            type_="tempore",
            token_preview="quo",
            workplace={"praesentium": 9},
        )
        self.assertEqual(test_model.slug, "laborum")
        self.assertEqual(test_model.name, "beatae")
        self.assertEqual(test_model.created_at, "reprehenderit")
        self.assertEqual(test_model.last_seen_at, "voluptatibus")
        self.assertEqual(test_model.type_, "tempore")
        self.assertEqual(test_model.token_preview, "quo")
        self.assertEqual(test_model.workplace, {"praesentium": 9})


if __name__ == "__main__":
    unittest.main()

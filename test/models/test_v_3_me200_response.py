import unittest
from src.dopplersdk.models.V3Me200Response import V3Me200Response


class TestV3Me200ResponseModel(unittest.TestCase):
    def test_true(self):
        self.assertTrue(True)

    def test_v_3_me200_response(self):
        # Create V3Me200Response class instance
        test_model = V3Me200Response(
            slug="modi",
            name="nulla",
            created_at="vitae",
            last_seen_at="doloremque",
            type_="dicta",
            token_preview="asperiores",
            workplace={"ad": 1},
        )
        self.assertEqual(test_model.slug, "modi")
        self.assertEqual(test_model.name, "nulla")
        self.assertEqual(test_model.created_at, "vitae")
        self.assertEqual(test_model.last_seen_at, "doloremque")
        self.assertEqual(test_model.type_, "dicta")
        self.assertEqual(test_model.token_preview, "asperiores")
        self.assertEqual(test_model.workplace, {"ad": 1})


if __name__ == "__main__":
    unittest.main()

import unittest
from src.dopplersdk.models.V3Me200Response import V3Me200Response


class TestV3Me200ResponseModel(unittest.TestCase):
    def test_true(self):
        self.assertTrue(True)

    def test_v_3_me200_response(self):
        # Create V3Me200Response class instance
        test_model = V3Me200Response(
            slug="qui",
            name="nisi",
            created_at="asperiores",
            last_seen_at="ex",
            type_="recusandae",
            token_preview="ex",
            workplace={"est": 1},
        )
        self.assertEqual(test_model.slug, "qui")
        self.assertEqual(test_model.name, "nisi")
        self.assertEqual(test_model.created_at, "asperiores")
        self.assertEqual(test_model.last_seen_at, "ex")
        self.assertEqual(test_model.type_, "recusandae")
        self.assertEqual(test_model.token_preview, "ex")
        self.assertEqual(test_model.workplace, {"est": 1})


if __name__ == "__main__":
    unittest.main()

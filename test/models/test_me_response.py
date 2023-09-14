import unittest
from src.dopplersdk.models.MeResponse import MeResponse


class TestMeResponseModel(unittest.TestCase):
    def test_true(self):
        self.assertTrue(True)

    def test_me_response(self):
        # Create MeResponse class instance
        test_model = MeResponse(
            slug="quasi",
            name="doloremque",
            created_at="consequatur",
            last_seen_at="quaerat",
            token_preview="totam",
            workplace={"quibusdam": 7},
            type_="praesentium",
        )
        self.assertEqual(test_model.slug, "quasi")
        self.assertEqual(test_model.name, "doloremque")
        self.assertEqual(test_model.created_at, "consequatur")
        self.assertEqual(test_model.last_seen_at, "quaerat")
        self.assertEqual(test_model.token_preview, "totam")
        self.assertEqual(test_model.workplace, {"quibusdam": 7})
        self.assertEqual(test_model.type_, "praesentium")


if __name__ == "__main__":
    unittest.main()

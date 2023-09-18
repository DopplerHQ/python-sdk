import unittest
from src.dopplersdk.models.MeResponse import MeResponse


class TestMeResponseModel(unittest.TestCase):
    def test_true(self):
        self.assertTrue(True)

    def test_me_response(self):
        # Create MeResponse class instance
        test_model = MeResponse(
            slug="saepe",
            name="harum",
            created_at="recusandae",
            last_seen_at="dolor",
            token_preview="consequuntur",
            workplace={"dolorem": 9},
            type_="eaque",
        )
        self.assertEqual(test_model.slug, "saepe")
        self.assertEqual(test_model.name, "harum")
        self.assertEqual(test_model.created_at, "recusandae")
        self.assertEqual(test_model.last_seen_at, "dolor")
        self.assertEqual(test_model.token_preview, "consequuntur")
        self.assertEqual(test_model.workplace, {"dolorem": 9})
        self.assertEqual(test_model.type_, "eaque")


if __name__ == "__main__":
    unittest.main()

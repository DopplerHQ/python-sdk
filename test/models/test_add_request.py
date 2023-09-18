import unittest
from src.dopplersdk.models.AddRequest import AddRequest


class TestAddRequestModel(unittest.TestCase):
    def test_true(self):
        self.assertTrue(True)

    def test_add_request(self):
        # Create AddRequest class instance
        test_model = AddRequest(
            type_="workplace_user",
            slug="optio",
            role="veniam",
            environments=["veniam", "libero"],
        )
        self.assertEqual(test_model.type_, "workplace_user")
        self.assertEqual(test_model.slug, "optio")
        self.assertEqual(test_model.role, "veniam")
        self.assertEqual(test_model.environments, ["veniam", "libero"])

    def test_add_request_required_fields_missing(self):
        # Assert AddRequest class generation fails without required fields
        with self.assertRaises(TypeError):
            test_model = AddRequest()


if __name__ == "__main__":
    unittest.main()

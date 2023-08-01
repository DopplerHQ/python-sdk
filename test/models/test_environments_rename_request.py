import unittest
from src.dopplersdk.models.EnvironmentsRenameRequest import EnvironmentsRenameRequest


class TestEnvironmentsRenameRequestModel(unittest.TestCase):
    def test_true(self):
        self.assertTrue(True)

    def test_environments_rename_request(self):
        # Create EnvironmentsRenameRequest class instance
        test_model = EnvironmentsRenameRequest(name="tenetur", slug="quod")
        self.assertEqual(test_model.name, "tenetur")
        self.assertEqual(test_model.slug, "quod")


if __name__ == "__main__":
    unittest.main()

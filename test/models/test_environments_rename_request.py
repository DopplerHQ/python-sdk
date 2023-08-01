import unittest
from src.dopplersdk.models.EnvironmentsRenameRequest import EnvironmentsRenameRequest


class TestEnvironmentsRenameRequestModel(unittest.TestCase):
    def test_true(self):
        self.assertTrue(True)

    def test_environments_rename_request(self):
        # Create EnvironmentsRenameRequest class instance
        test_model = EnvironmentsRenameRequest(name="praesentium", slug="dolor")
        self.assertEqual(test_model.name, "praesentium")
        self.assertEqual(test_model.slug, "dolor")


if __name__ == "__main__":
    unittest.main()

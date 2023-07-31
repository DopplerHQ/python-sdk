import unittest
from src.dopplersdk.models.EnvironmentsRenameRequest import EnvironmentsRenameRequest


class TestEnvironmentsRenameRequestModel(unittest.TestCase):
    def test_true(self):
        self.assertTrue(True)

    def test_environments_rename_request(self):
        # Create EnvironmentsRenameRequest class instance
        test_model = EnvironmentsRenameRequest(name="omnis", slug="esse")
        self.assertEqual(test_model.name, "omnis")
        self.assertEqual(test_model.slug, "esse")


if __name__ == "__main__":
    unittest.main()

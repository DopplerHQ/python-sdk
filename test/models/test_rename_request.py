import unittest
from src.dopplersdk.models.RenameRequest import RenameRequest


class TestRenameRequestModel(unittest.TestCase):
    def test_true(self):
        self.assertTrue(True)

    def test_rename_request(self):
        # Create RenameRequest class instance
        test_model = RenameRequest(name="aliquam", slug="vel")
        self.assertEqual(test_model.name, "aliquam")
        self.assertEqual(test_model.slug, "vel")


if __name__ == "__main__":
    unittest.main()

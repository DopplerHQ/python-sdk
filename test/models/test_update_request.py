import unittest
from src.dopplersdk.models.UpdateRequest import UpdateRequest


class TestUpdateRequestModel(unittest.TestCase):
    def test_true(self):
        self.assertTrue(True)

    def test_update_request(self):
        # Create UpdateRequest class instance
        test_model = UpdateRequest(name="asperiores", default_project_role="ducimus")
        self.assertEqual(test_model.name, "asperiores")
        self.assertEqual(test_model.default_project_role, "ducimus")


if __name__ == "__main__":
    unittest.main()

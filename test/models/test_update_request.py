import unittest
from src.dopplersdk.models.UpdateRequest import UpdateRequest


class TestUpdateRequestModel(unittest.TestCase):
    def test_true(self):
        self.assertTrue(True)

    def test_update_request(self):
        # Create UpdateRequest class instance
        test_model = UpdateRequest(name="quaerat", default_project_role="mollitia")
        self.assertEqual(test_model.name, "quaerat")
        self.assertEqual(test_model.default_project_role, "mollitia")


if __name__ == "__main__":
    unittest.main()

import unittest
from src.dopplersdk.models.UpdateResponse import UpdateResponse


class TestUpdateResponseModel(unittest.TestCase):
    def test_true(self):
        self.assertTrue(True)

    def test_update_response(self):
        # Create UpdateResponse class instance
        test_model = UpdateResponse(project={"neque": 4})
        self.assertEqual(test_model.project, {"neque": 4})


if __name__ == "__main__":
    unittest.main()

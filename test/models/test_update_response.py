import unittest
from src.dopplersdk.models.UpdateResponse import UpdateResponse


class TestUpdateResponseModel(unittest.TestCase):
    def test_true(self):
        self.assertTrue(True)

    def test_update_response(self):
        # Create UpdateResponse class instance
        test_model = UpdateResponse(secrets={"aut": 9})
        self.assertEqual(test_model.secrets, {"aut": 9})


if __name__ == "__main__":
    unittest.main()

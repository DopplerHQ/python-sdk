import unittest
from src.dopplersdk.models.DeleteResponse import DeleteResponse


class TestDeleteResponseModel(unittest.TestCase):
    def test_true(self):
        self.assertTrue(True)

    def test_delete_response(self):
        # Create DeleteResponse class instance
        test_model = DeleteResponse(success=True)
        self.assertEqual(test_model.success, True)


if __name__ == "__main__":
    unittest.main()

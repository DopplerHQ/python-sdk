import unittest
from src.dopplersdk.models.RollbackResponse import RollbackResponse


class TestRollbackResponseModel(unittest.TestCase):
    def test_true(self):
        self.assertTrue(True)

    def test_rollback_response(self):
        # Create RollbackResponse class instance
        test_model = RollbackResponse(log={"nobis": 9})
        self.assertEqual(test_model.log, {"nobis": 9})


if __name__ == "__main__":
    unittest.main()

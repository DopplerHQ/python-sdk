import unittest
from src.dopplersdk.models.LockResponse import LockResponse


class TestLockResponseModel(unittest.TestCase):
    def test_true(self):
        self.assertTrue(True)

    def test_lock_response(self):
        # Create LockResponse class instance
        test_model = LockResponse(config={"veritatis": 6})
        self.assertEqual(test_model.config, {"veritatis": 6})


if __name__ == "__main__":
    unittest.main()

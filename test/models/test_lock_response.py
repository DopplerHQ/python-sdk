import unittest
from src.dopplersdk.models.LockResponse import LockResponse


class TestLockResponseModel(unittest.TestCase):
    def test_true(self):
        self.assertTrue(True)

    def test_lock_response(self):
        # Create LockResponse class instance
        test_model = LockResponse(config={"ex": 8})
        self.assertEqual(test_model.config, {"ex": 8})


if __name__ == "__main__":
    unittest.main()

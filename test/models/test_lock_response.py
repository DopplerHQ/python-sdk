import unittest
from src.dopplersdk.models.LockResponse import LockResponse


class TestLockResponseModel(unittest.TestCase):
    def test_true(self):
        self.assertTrue(True)

    def test_lock_response(self):
        # Create LockResponse class instance
        test_model = LockResponse(config={"hic": 8})
        self.assertEqual(test_model.config, {"hic": 8})


if __name__ == "__main__":
    unittest.main()

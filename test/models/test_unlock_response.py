import unittest
from src.dopplersdk.models.UnlockResponse import UnlockResponse


class TestUnlockResponseModel(unittest.TestCase):
    def test_true(self):
        self.assertTrue(True)

    def test_unlock_response(self):
        # Create UnlockResponse class instance
        test_model = UnlockResponse(config={"asperiores": 2})
        self.assertEqual(test_model.config, {"asperiores": 2})


if __name__ == "__main__":
    unittest.main()

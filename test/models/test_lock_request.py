import unittest
from src.dopplersdk.models.LockRequest import LockRequest


class TestLockRequestModel(unittest.TestCase):
    def test_true(self):
        self.assertTrue(True)

    def test_lock_request(self):
        # Create LockRequest class instance
        test_model = LockRequest(config="eligendi", project="error")
        self.assertEqual(test_model.config, "eligendi")
        self.assertEqual(test_model.project, "error")

    def test_lock_request_required_fields_missing(self):
        # Assert LockRequest class generation fails without required fields
        with self.assertRaises(TypeError):
            test_model = LockRequest()


if __name__ == "__main__":
    unittest.main()

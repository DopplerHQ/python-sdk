import unittest
from src.dopplersdk.models.RevokeLeaseResponse import RevokeLeaseResponse


class TestRevokeLeaseResponseModel(unittest.TestCase):
    def test_true(self):
        self.assertTrue(True)

    def test_revoke_lease_response(self):
        # Create RevokeLeaseResponse class instance
        test_model = RevokeLeaseResponse(success=True)
        self.assertEqual(test_model.success, True)


if __name__ == "__main__":
    unittest.main()

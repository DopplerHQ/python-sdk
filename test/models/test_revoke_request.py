import unittest
from src.dopplersdk.models.RevokeRequest import RevokeRequest


class TestRevokeRequestModel(unittest.TestCase):
    def test_true(self):
        self.assertTrue(True)

    def test_revoke_request(self):
        # Create RevokeRequest class instance
        test_model = RevokeRequest(token="delectus")
        self.assertEqual(test_model.token, "delectus")

    def test_revoke_request_required_fields_missing(self):
        # Assert RevokeRequest class generation fails without required fields
        with self.assertRaises(TypeError):
            test_model = RevokeRequest()


if __name__ == "__main__":
    unittest.main()

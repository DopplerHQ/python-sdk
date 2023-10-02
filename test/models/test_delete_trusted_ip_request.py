import unittest
from src.dopplersdk.models.DeleteTrustedIpRequest import DeleteTrustedIpRequest


class TestDeleteTrustedIpRequestModel(unittest.TestCase):
    def test_true(self):
        self.assertTrue(True)

    def test_delete_trusted_ip_request(self):
        # Create DeleteTrustedIpRequest class instance
        test_model = DeleteTrustedIpRequest(ip="ipsam")
        self.assertEqual(test_model.ip, "ipsam")

    def test_delete_trusted_ip_request_required_fields_missing(self):
        # Assert DeleteTrustedIpRequest class generation fails without required fields
        with self.assertRaises(TypeError):
            test_model = DeleteTrustedIpRequest()


if __name__ == "__main__":
    unittest.main()

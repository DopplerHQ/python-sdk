import unittest
from src.dopplersdk.models.AddTrustedIpRequest import AddTrustedIpRequest


class TestAddTrustedIpRequestModel(unittest.TestCase):
    def test_true(self):
        self.assertTrue(True)

    def test_add_trusted_ip_request(self):
        # Create AddTrustedIpRequest class instance
        test_model = AddTrustedIpRequest(ip="quasi")
        self.assertEqual(test_model.ip, "quasi")

    def test_add_trusted_ip_request_required_fields_missing(self):
        # Assert AddTrustedIpRequest class generation fails without required fields
        with self.assertRaises(TypeError):
            test_model = AddTrustedIpRequest()


if __name__ == "__main__":
    unittest.main()

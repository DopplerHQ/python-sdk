import unittest
from src.dopplersdk.models.AddTrustedIpResponse import AddTrustedIpResponse


class TestAddTrustedIpResponseModel(unittest.TestCase):
    def test_true(self):
        self.assertTrue(True)

    def test_add_trusted_ip_response(self):
        # Create AddTrustedIpResponse class instance
        test_model = AddTrustedIpResponse(ip="ab")
        self.assertEqual(test_model.ip, "ab")


if __name__ == "__main__":
    unittest.main()

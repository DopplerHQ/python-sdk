import unittest
from src.dopplersdk.models.ListTrustedIpsResponse import ListTrustedIpsResponse


class TestListTrustedIpsResponseModel(unittest.TestCase):
    def test_true(self):
        self.assertTrue(True)

    def test_list_trusted_ips_response(self):
        # Create ListTrustedIpsResponse class instance
        test_model = ListTrustedIpsResponse(ips=["eveniet", "fugiat"])
        self.assertEqual(test_model.ips, ["eveniet", "fugiat"])


if __name__ == "__main__":
    unittest.main()

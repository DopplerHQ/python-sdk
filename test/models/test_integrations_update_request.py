import unittest
from src.dopplersdk.models.IntegrationsUpdateRequest import IntegrationsUpdateRequest


class TestIntegrationsUpdateRequestModel(unittest.TestCase):
    def test_true(self):
        self.assertTrue(True)

    def test_integrations_update_request(self):
        # Create IntegrationsUpdateRequest class instance
        test_model = IntegrationsUpdateRequest(name="voluptate", data="iure")
        self.assertEqual(test_model.name, "voluptate")
        self.assertEqual(test_model.data, "iure")


if __name__ == "__main__":
    unittest.main()

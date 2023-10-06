import unittest
from src.dopplersdk.models.IntegrationsUpdateRequest import IntegrationsUpdateRequest


class TestIntegrationsUpdateRequestModel(unittest.TestCase):
    def test_true(self):
        self.assertTrue(True)

    def test_integrations_update_request(self):
        # Create IntegrationsUpdateRequest class instance
        test_model = IntegrationsUpdateRequest(name="saepe", data="tenetur")
        self.assertEqual(test_model.name, "saepe")
        self.assertEqual(test_model.data, "tenetur")


if __name__ == "__main__":
    unittest.main()

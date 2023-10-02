import unittest
from src.dopplersdk.models.IntegrationsUpdateRequest import IntegrationsUpdateRequest


class TestIntegrationsUpdateRequestModel(unittest.TestCase):
    def test_true(self):
        self.assertTrue(True)

    def test_integrations_update_request(self):
        # Create IntegrationsUpdateRequest class instance
        test_model = IntegrationsUpdateRequest(name="quidem", data="quam")
        self.assertEqual(test_model.name, "quidem")
        self.assertEqual(test_model.data, "quam")


if __name__ == "__main__":
    unittest.main()

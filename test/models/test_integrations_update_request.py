import unittest
from src.dopplersdk.models.IntegrationsUpdateRequest import IntegrationsUpdateRequest


class TestIntegrationsUpdateRequestModel(unittest.TestCase):
    def test_true(self):
        self.assertTrue(True)

    def test_integrations_update_request(self):
        # Create IntegrationsUpdateRequest class instance
        test_model = IntegrationsUpdateRequest(name="corrupti", data="voluptatem")
        self.assertEqual(test_model.name, "corrupti")
        self.assertEqual(test_model.data, "voluptatem")


if __name__ == "__main__":
    unittest.main()

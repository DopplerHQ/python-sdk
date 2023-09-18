import unittest
from src.dopplersdk.models.IntegrationsCreateResponse import IntegrationsCreateResponse


class TestIntegrationsCreateResponseModel(unittest.TestCase):
    def test_true(self):
        self.assertTrue(True)

    def test_integrations_create_response(self):
        # Create IntegrationsCreateResponse class instance
        test_model = IntegrationsCreateResponse(integration={"harum": 3})
        self.assertEqual(test_model.integration, {"harum": 3})


if __name__ == "__main__":
    unittest.main()

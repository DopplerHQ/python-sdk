import unittest
from src.dopplersdk.models.IntegrationsCreateResponse import IntegrationsCreateResponse


class TestIntegrationsCreateResponseModel(unittest.TestCase):
    def test_true(self):
        self.assertTrue(True)

    def test_integrations_create_response(self):
        # Create IntegrationsCreateResponse class instance
        test_model = IntegrationsCreateResponse(integration={"laudantium": 2})
        self.assertEqual(test_model.integration, {"laudantium": 2})


if __name__ == "__main__":
    unittest.main()

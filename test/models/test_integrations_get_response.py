import unittest
from src.dopplersdk.models.IntegrationsGetResponse import IntegrationsGetResponse


class TestIntegrationsGetResponseModel(unittest.TestCase):
    def test_true(self):
        self.assertTrue(True)

    def test_integrations_get_response(self):
        # Create IntegrationsGetResponse class instance
        test_model = IntegrationsGetResponse(integration={"voluptas": 2})
        self.assertEqual(test_model.integration, {"voluptas": 2})


if __name__ == "__main__":
    unittest.main()

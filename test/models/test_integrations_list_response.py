import unittest
from src.dopplersdk.models.IntegrationsListResponse import IntegrationsListResponse


class TestIntegrationsListResponseModel(unittest.TestCase):
    def test_true(self):
        self.assertTrue(True)

    def test_integrations_list_response(self):
        # Create IntegrationsListResponse class instance
        test_model = IntegrationsListResponse(
            integrations=["reprehenderit", "reiciendis"], success=True
        )
        self.assertEqual(test_model.integrations, ["reprehenderit", "reiciendis"])
        self.assertEqual(test_model.success, True)


if __name__ == "__main__":
    unittest.main()

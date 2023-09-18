import unittest
from src.dopplersdk.models.IntegrationsCreateRequest import IntegrationsCreateRequest


class TestIntegrationsCreateRequestModel(unittest.TestCase):
    def test_true(self):
        self.assertTrue(True)

    def test_integrations_create_request(self):
        # Create IntegrationsCreateRequest class instance
        test_model = IntegrationsCreateRequest(
            type_="eveniet", name="repudiandae", data={"debitis": 3}
        )
        self.assertEqual(test_model.type_, "eveniet")
        self.assertEqual(test_model.name, "repudiandae")
        self.assertEqual(test_model.data, {"debitis": 3})

    def test_integrations_create_request_required_fields_missing(self):
        # Assert IntegrationsCreateRequest class generation fails without required fields
        with self.assertRaises(TypeError):
            test_model = IntegrationsCreateRequest()


if __name__ == "__main__":
    unittest.main()

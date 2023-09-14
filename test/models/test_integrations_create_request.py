import unittest
from src.dopplersdk.models.IntegrationsCreateRequest import IntegrationsCreateRequest


class TestIntegrationsCreateRequestModel(unittest.TestCase):
    def test_true(self):
        self.assertTrue(True)

    def test_integrations_create_request(self):
        # Create IntegrationsCreateRequest class instance
        test_model = IntegrationsCreateRequest(
            type_="officia", name="quibusdam", data={"dolores": 8}
        )
        self.assertEqual(test_model.type_, "officia")
        self.assertEqual(test_model.name, "quibusdam")
        self.assertEqual(test_model.data, {"dolores": 8})

    def test_integrations_create_request_required_fields_missing(self):
        # Assert IntegrationsCreateRequest class generation fails without required fields
        with self.assertRaises(TypeError):
            test_model = IntegrationsCreateRequest()


if __name__ == "__main__":
    unittest.main()

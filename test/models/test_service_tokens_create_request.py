import unittest
from src.dopplersdk.models.ServiceTokensCreateRequest import ServiceTokensCreateRequest


class TestServiceTokensCreateRequestModel(unittest.TestCase):
    def test_true(self):
        self.assertTrue(True)

    def test_service_tokens_create_request(self):
        # Create ServiceTokensCreateRequest class instance
        test_model = ServiceTokensCreateRequest(
            name="voluptatum",
            config="pariatur",
            project="vel",
            expire_at="quos",
            access="read",
        )
        self.assertEqual(test_model.name, "voluptatum")
        self.assertEqual(test_model.config, "pariatur")
        self.assertEqual(test_model.project, "vel")
        self.assertEqual(test_model.expire_at, "quos")
        self.assertEqual(test_model.access, "read")

    def test_service_tokens_create_request_required_fields_missing(self):
        # Assert ServiceTokensCreateRequest class generation fails without required fields
        with self.assertRaises(TypeError):
            test_model = ServiceTokensCreateRequest()


if __name__ == "__main__":
    unittest.main()

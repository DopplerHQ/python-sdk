import unittest
from src.dopplersdk.models.ServiceTokensCreateRequest import ServiceTokensCreateRequest


class TestServiceTokensCreateRequestModel(unittest.TestCase):
    def test_true(self):
        self.assertTrue(True)

    def test_service_tokens_create_request(self):
        # Create ServiceTokensCreateRequest class instance
        test_model = ServiceTokensCreateRequest(
            name="tenetur",
            config="minus",
            project="necessitatibus",
            expire_at="debitis",
            access="read",
        )
        self.assertEqual(test_model.name, "tenetur")
        self.assertEqual(test_model.config, "minus")
        self.assertEqual(test_model.project, "necessitatibus")
        self.assertEqual(test_model.expire_at, "debitis")
        self.assertEqual(test_model.access, "read")

    def test_service_tokens_create_request_required_fields_missing(self):
        # Assert ServiceTokensCreateRequest class generation fails without required fields
        with self.assertRaises(TypeError):
            test_model = ServiceTokensCreateRequest()


if __name__ == "__main__":
    unittest.main()

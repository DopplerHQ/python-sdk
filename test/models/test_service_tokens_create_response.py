import unittest
from src.dopplersdk.models.ServiceTokensCreateResponse import (
    ServiceTokensCreateResponse,
)


class TestServiceTokensCreateResponseModel(unittest.TestCase):
    def test_true(self):
        self.assertTrue(True)

    def test_service_tokens_create_response(self):
        # Create ServiceTokensCreateResponse class instance
        test_model = ServiceTokensCreateResponse(
            name="vitae",
            slug="minima",
            created_at="eum",
            key="explicabo",
            config="provident",
            environment="vitae",
            project="dignissimos",
            expires_at="foo",
            access="voluptates",
        )
        self.assertEqual(test_model.name, "vitae")
        self.assertEqual(test_model.slug, "minima")
        self.assertEqual(test_model.created_at, "eum")
        self.assertEqual(test_model.key, "explicabo")
        self.assertEqual(test_model.config, "provident")
        self.assertEqual(test_model.environment, "vitae")
        self.assertEqual(test_model.project, "dignissimos")
        self.assertEqual(test_model.expires_at, "foo")
        self.assertEqual(test_model.access, "voluptates")


if __name__ == "__main__":
    unittest.main()

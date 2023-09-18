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
            name="odio",
            slug="provident",
            created_at="natus",
            key="ab",
            config="porro",
            environment="at",
            project="voluptas",
            expires_at="foo",
            access="quam",
        )
        self.assertEqual(test_model.name, "odio")
        self.assertEqual(test_model.slug, "provident")
        self.assertEqual(test_model.created_at, "natus")
        self.assertEqual(test_model.key, "ab")
        self.assertEqual(test_model.config, "porro")
        self.assertEqual(test_model.environment, "at")
        self.assertEqual(test_model.project, "voluptas")
        self.assertEqual(test_model.expires_at, "foo")
        self.assertEqual(test_model.access, "quam")


if __name__ == "__main__":
    unittest.main()

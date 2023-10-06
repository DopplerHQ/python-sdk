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
            name="molestiae",
            slug="non",
            created_at="eligendi",
            key="aut",
            config="occaecati",
            environment="dignissimos",
            project="dolor",
            expires_at="foo",
            access="ut",
        )
        self.assertEqual(test_model.name, "molestiae")
        self.assertEqual(test_model.slug, "non")
        self.assertEqual(test_model.created_at, "eligendi")
        self.assertEqual(test_model.key, "aut")
        self.assertEqual(test_model.config, "occaecati")
        self.assertEqual(test_model.environment, "dignissimos")
        self.assertEqual(test_model.project, "dolor")
        self.assertEqual(test_model.expires_at, "foo")
        self.assertEqual(test_model.access, "ut")


if __name__ == "__main__":
    unittest.main()

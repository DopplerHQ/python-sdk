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
            name="debitis",
            slug="exercitationem",
            created_at="quia",
            key="odit",
            config="dolor",
            environment="occaecati",
            project="doloremque",
            expires_at="foo",
            access="iusto",
        )
        self.assertEqual(test_model.name, "debitis")
        self.assertEqual(test_model.slug, "exercitationem")
        self.assertEqual(test_model.created_at, "quia")
        self.assertEqual(test_model.key, "odit")
        self.assertEqual(test_model.config, "dolor")
        self.assertEqual(test_model.environment, "occaecati")
        self.assertEqual(test_model.project, "doloremque")
        self.assertEqual(test_model.expires_at, "foo")
        self.assertEqual(test_model.access, "iusto")


if __name__ == "__main__":
    unittest.main()

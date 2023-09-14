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
            name="nobis",
            slug="ducimus",
            created_at="animi",
            key="reprehenderit",
            config="sequi",
            environment="explicabo",
            project="amet",
            expires_at="foo",
            access="illum",
        )
        self.assertEqual(test_model.name, "nobis")
        self.assertEqual(test_model.slug, "ducimus")
        self.assertEqual(test_model.created_at, "animi")
        self.assertEqual(test_model.key, "reprehenderit")
        self.assertEqual(test_model.config, "sequi")
        self.assertEqual(test_model.environment, "explicabo")
        self.assertEqual(test_model.project, "amet")
        self.assertEqual(test_model.expires_at, "foo")
        self.assertEqual(test_model.access, "illum")


if __name__ == "__main__":
    unittest.main()

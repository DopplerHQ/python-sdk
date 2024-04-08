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
            slug="consequuntur",
            created_at="similique",
            key="architecto",
            config="nobis",
            environment="nesciunt",
            project="voluptatem",
            expires_at="foo",
            access="accusantium",
        )
        self.assertEqual(test_model.name, "nobis")
        self.assertEqual(test_model.slug, "consequuntur")
        self.assertEqual(test_model.created_at, "similique")
        self.assertEqual(test_model.key, "architecto")
        self.assertEqual(test_model.config, "nobis")
        self.assertEqual(test_model.environment, "nesciunt")
        self.assertEqual(test_model.project, "voluptatem")
        self.assertEqual(test_model.expires_at, "foo")
        self.assertEqual(test_model.access, "accusantium")


if __name__ == "__main__":
    unittest.main()

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
            name="quis",
            slug="nulla",
            created_at="aliquam",
            key="possimus",
            config="praesentium",
            environment="consequuntur",
            project="illo",
            expires_at="foo",
            access="repellat",
        )
        self.assertEqual(test_model.name, "quis")
        self.assertEqual(test_model.slug, "nulla")
        self.assertEqual(test_model.created_at, "aliquam")
        self.assertEqual(test_model.key, "possimus")
        self.assertEqual(test_model.config, "praesentium")
        self.assertEqual(test_model.environment, "consequuntur")
        self.assertEqual(test_model.project, "illo")
        self.assertEqual(test_model.expires_at, "foo")
        self.assertEqual(test_model.access, "repellat")


if __name__ == "__main__":
    unittest.main()

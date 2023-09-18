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
            name="porro",
            slug="similique",
            created_at="iusto",
            key="maxime",
            config="ad",
            environment="ducimus",
            project="eligendi",
            expires_at="foo",
            access="delectus",
        )
        self.assertEqual(test_model.name, "porro")
        self.assertEqual(test_model.slug, "similique")
        self.assertEqual(test_model.created_at, "iusto")
        self.assertEqual(test_model.key, "maxime")
        self.assertEqual(test_model.config, "ad")
        self.assertEqual(test_model.environment, "ducimus")
        self.assertEqual(test_model.project, "eligendi")
        self.assertEqual(test_model.expires_at, "foo")
        self.assertEqual(test_model.access, "delectus")


if __name__ == "__main__":
    unittest.main()

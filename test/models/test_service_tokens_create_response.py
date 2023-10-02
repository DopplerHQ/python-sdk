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
            name="blanditiis",
            slug="eius",
            created_at="expedita",
            key="commodi",
            config="dicta",
            environment="quia",
            project="officia",
            expires_at="foo",
            access="earum",
        )
        self.assertEqual(test_model.name, "blanditiis")
        self.assertEqual(test_model.slug, "eius")
        self.assertEqual(test_model.created_at, "expedita")
        self.assertEqual(test_model.key, "commodi")
        self.assertEqual(test_model.config, "dicta")
        self.assertEqual(test_model.environment, "quia")
        self.assertEqual(test_model.project, "officia")
        self.assertEqual(test_model.expires_at, "foo")
        self.assertEqual(test_model.access, "earum")


if __name__ == "__main__":
    unittest.main()

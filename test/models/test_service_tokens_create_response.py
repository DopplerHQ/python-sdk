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
            name="voluptatum",
            slug="repellat",
            created_at="consectetur",
            key="neque",
            config="inventore",
            environment="commodi",
            project="magni",
            expires_at="foo",
            access="laborum",
        )
        self.assertEqual(test_model.name, "voluptatum")
        self.assertEqual(test_model.slug, "repellat")
        self.assertEqual(test_model.created_at, "consectetur")
        self.assertEqual(test_model.key, "neque")
        self.assertEqual(test_model.config, "inventore")
        self.assertEqual(test_model.environment, "commodi")
        self.assertEqual(test_model.project, "magni")
        self.assertEqual(test_model.expires_at, "foo")
        self.assertEqual(test_model.access, "laborum")


if __name__ == "__main__":
    unittest.main()

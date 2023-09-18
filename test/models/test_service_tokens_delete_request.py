import unittest
from src.dopplersdk.models.ServiceTokensDeleteRequest import ServiceTokensDeleteRequest


class TestServiceTokensDeleteRequestModel(unittest.TestCase):
    def test_true(self):
        self.assertTrue(True)

    def test_service_tokens_delete_request(self):
        # Create ServiceTokensDeleteRequest class instance
        test_model = ServiceTokensDeleteRequest(
            config="dolor", project="corporis", slug="et", token="perspiciatis"
        )
        self.assertEqual(test_model.config, "dolor")
        self.assertEqual(test_model.project, "corporis")
        self.assertEqual(test_model.slug, "et")
        self.assertEqual(test_model.token, "perspiciatis")

    def test_service_tokens_delete_request_required_fields_missing(self):
        # Assert ServiceTokensDeleteRequest class generation fails without required fields
        with self.assertRaises(TypeError):
            test_model = ServiceTokensDeleteRequest()


if __name__ == "__main__":
    unittest.main()

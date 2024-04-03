import unittest
from src.dopplersdk.models.ServiceTokensDeleteRequest import ServiceTokensDeleteRequest


class TestServiceTokensDeleteRequestModel(unittest.TestCase):
    def test_true(self):
        self.assertTrue(True)

    def test_service_tokens_delete_request(self):
        # Create ServiceTokensDeleteRequest class instance
        test_model = ServiceTokensDeleteRequest(
            config="sed", project="alias", slug="quidem", token="iusto"
        )
        self.assertEqual(test_model.config, "sed")
        self.assertEqual(test_model.project, "alias")
        self.assertEqual(test_model.slug, "quidem")
        self.assertEqual(test_model.token, "iusto")

    def test_service_tokens_delete_request_required_fields_missing(self):
        # Assert ServiceTokensDeleteRequest class generation fails without required fields
        with self.assertRaises(TypeError):
            test_model = ServiceTokensDeleteRequest()


if __name__ == "__main__":
    unittest.main()

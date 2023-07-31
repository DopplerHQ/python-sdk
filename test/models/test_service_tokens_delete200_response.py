import unittest
from src.dopplersdk.models.ServiceTokensDelete200Response import (
    ServiceTokensDelete200Response,
)


class TestServiceTokensDelete200ResponseModel(unittest.TestCase):
    def test_true(self):
        self.assertTrue(True)

    def test_service_tokens_delete200_response(self):
        # Create ServiceTokensDelete200Response class instance
        test_model = ServiceTokensDelete200Response(success=True)
        self.assertEqual(test_model.success, True)


if __name__ == "__main__":
    unittest.main()

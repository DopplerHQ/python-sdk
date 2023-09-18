import unittest
from src.dopplersdk.models.ServiceTokensListResponse import ServiceTokensListResponse


class TestServiceTokensListResponseModel(unittest.TestCase):
    def test_true(self):
        self.assertTrue(True)

    def test_service_tokens_list_response(self):
        # Create ServiceTokensListResponse class instance
        test_model = ServiceTokensListResponse(tokens=["consectetur", "possimus"])
        self.assertEqual(test_model.tokens, ["consectetur", "possimus"])


if __name__ == "__main__":
    unittest.main()

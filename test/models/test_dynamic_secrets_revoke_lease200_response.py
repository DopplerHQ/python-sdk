import unittest
from src.dopplersdk.models.DynamicSecretsRevokeLease200Response import (
    DynamicSecretsRevokeLease200Response,
)


class TestDynamicSecretsRevokeLease200ResponseModel(unittest.TestCase):
    def test_true(self):
        self.assertTrue(True)

    def test_dynamic_secrets_revoke_lease200_response(self):
        # Create DynamicSecretsRevokeLease200Response class instance
        test_model = DynamicSecretsRevokeLease200Response(success=True)
        self.assertEqual(test_model.success, True)


if __name__ == "__main__":
    unittest.main()

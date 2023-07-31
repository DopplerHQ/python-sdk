import unittest
from src.dopplersdk.models.ConfigsDelete200Response import ConfigsDelete200Response


class TestConfigsDelete200ResponseModel(unittest.TestCase):
    def test_true(self):
        self.assertTrue(True)

    def test_configs_delete200_response(self):
        # Create ConfigsDelete200Response class instance
        test_model = ConfigsDelete200Response(success=True)
        self.assertEqual(test_model.success, True)


if __name__ == "__main__":
    unittest.main()

import unittest
from src.dopplersdk.models.ConfigsCreate200Response import ConfigsCreate200Response


class TestConfigsCreate200ResponseModel(unittest.TestCase):
    def test_true(self):
        self.assertTrue(True)

    def test_configs_create200_response(self):
        # Create ConfigsCreate200Response class instance
        test_model = ConfigsCreate200Response(config={"provident": 6})
        self.assertEqual(test_model.config, {"provident": 6})


if __name__ == "__main__":
    unittest.main()

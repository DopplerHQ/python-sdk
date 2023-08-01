import unittest
from src.dopplersdk.models.ConfigsGet200Response import ConfigsGet200Response


class TestConfigsGet200ResponseModel(unittest.TestCase):
    def test_true(self):
        self.assertTrue(True)

    def test_configs_get200_response(self):
        # Create ConfigsGet200Response class instance
        test_model = ConfigsGet200Response(config={"ab": 7})
        self.assertEqual(test_model.config, {"ab": 7})


if __name__ == "__main__":
    unittest.main()

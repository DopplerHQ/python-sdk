import unittest
from src.dopplersdk.models.ConfigsCreateResponse import ConfigsCreateResponse


class TestConfigsCreateResponseModel(unittest.TestCase):
    def test_true(self):
        self.assertTrue(True)

    def test_configs_create_response(self):
        # Create ConfigsCreateResponse class instance
        test_model = ConfigsCreateResponse(config={"deserunt": 7})
        self.assertEqual(test_model.config, {"deserunt": 7})


if __name__ == "__main__":
    unittest.main()

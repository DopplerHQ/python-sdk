import unittest
from src.dopplersdk.models.ConfigsCreateResponse import ConfigsCreateResponse


class TestConfigsCreateResponseModel(unittest.TestCase):
    def test_true(self):
        self.assertTrue(True)

    def test_configs_create_response(self):
        # Create ConfigsCreateResponse class instance
        test_model = ConfigsCreateResponse(config={"quos": 9})
        self.assertEqual(test_model.config, {"quos": 9})


if __name__ == "__main__":
    unittest.main()

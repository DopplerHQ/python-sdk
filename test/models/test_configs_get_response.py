import unittest
from src.dopplersdk.models.ConfigsGetResponse import ConfigsGetResponse


class TestConfigsGetResponseModel(unittest.TestCase):
    def test_true(self):
        self.assertTrue(True)

    def test_configs_get_response(self):
        # Create ConfigsGetResponse class instance
        test_model = ConfigsGetResponse(config={"deleniti": 5})
        self.assertEqual(test_model.config, {"deleniti": 5})


if __name__ == "__main__":
    unittest.main()

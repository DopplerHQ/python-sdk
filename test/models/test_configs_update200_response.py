import unittest
from src.dopplersdk.models.ConfigsUpdate200Response import ConfigsUpdate200Response


class TestConfigsUpdate200ResponseModel(unittest.TestCase):
    def test_true(self):
        self.assertTrue(True)

    def test_configs_update200_response(self):
        # Create ConfigsUpdate200Response class instance
        test_model = ConfigsUpdate200Response(config={"vero": 6})
        self.assertEqual(test_model.config, {"vero": 6})


if __name__ == "__main__":
    unittest.main()

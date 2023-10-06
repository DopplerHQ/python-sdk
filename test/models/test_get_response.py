import unittest
from src.dopplersdk.models.GetResponse import GetResponse


class TestGetResponseModel(unittest.TestCase):
    def test_true(self):
        self.assertTrue(True)

    def test_get_response(self):
        # Create GetResponse class instance
        test_model = GetResponse(log={"architecto": 6})
        self.assertEqual(test_model.log, {"architecto": 6})


if __name__ == "__main__":
    unittest.main()

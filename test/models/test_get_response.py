import unittest
from src.dopplersdk.models.GetResponse import GetResponse


class TestGetResponseModel(unittest.TestCase):
    def test_true(self):
        self.assertTrue(True)

    def test_get_response(self):
        # Create GetResponse class instance
        test_model = GetResponse(group={"odio": 9})
        self.assertEqual(test_model.group, {"odio": 9})


if __name__ == "__main__":
    unittest.main()

import unittest
from src.dopplersdk.models.CloneResponse import CloneResponse


class TestCloneResponseModel(unittest.TestCase):
    def test_true(self):
        self.assertTrue(True)

    def test_clone_response(self):
        # Create CloneResponse class instance
        test_model = CloneResponse(config={"alias": 6})
        self.assertEqual(test_model.config, {"alias": 6})


if __name__ == "__main__":
    unittest.main()

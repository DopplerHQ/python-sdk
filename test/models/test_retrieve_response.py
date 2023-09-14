import unittest
from src.dopplersdk.models.RetrieveResponse import RetrieveResponse


class TestRetrieveResponseModel(unittest.TestCase):
    def test_true(self):
        self.assertTrue(True)

    def test_retrieve_response(self):
        # Create RetrieveResponse class instance
        test_model = RetrieveResponse(log={"reiciendis": 2})
        self.assertEqual(test_model.log, {"reiciendis": 2})


if __name__ == "__main__":
    unittest.main()

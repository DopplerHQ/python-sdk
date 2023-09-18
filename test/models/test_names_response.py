import unittest
from src.dopplersdk.models.NamesResponse import NamesResponse


class TestNamesResponseModel(unittest.TestCase):
    def test_true(self):
        self.assertTrue(True)

    def test_names_response(self):
        # Create NamesResponse class instance
        test_model = NamesResponse(names=["distinctio", "nemo"])
        self.assertEqual(test_model.names, ["distinctio", "nemo"])


if __name__ == "__main__":
    unittest.main()

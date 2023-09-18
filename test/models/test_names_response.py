import unittest
from src.dopplersdk.models.NamesResponse import NamesResponse


class TestNamesResponseModel(unittest.TestCase):
    def test_true(self):
        self.assertTrue(True)

    def test_names_response(self):
        # Create NamesResponse class instance
        test_model = NamesResponse(names=["est", "ipsam"])
        self.assertEqual(test_model.names, ["est", "ipsam"])


if __name__ == "__main__":
    unittest.main()

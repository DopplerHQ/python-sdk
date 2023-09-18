import unittest
from src.dopplersdk.models.NamesResponse import NamesResponse


class TestNamesResponseModel(unittest.TestCase):
    def test_true(self):
        self.assertTrue(True)

    def test_names_response(self):
        # Create NamesResponse class instance
        test_model = NamesResponse(names=["commodi", "impedit"])
        self.assertEqual(test_model.names, ["commodi", "impedit"])


if __name__ == "__main__":
    unittest.main()

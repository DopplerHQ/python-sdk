import unittest
from src.dopplersdk.models.AddResponse import AddResponse


class TestAddResponseModel(unittest.TestCase):
    def test_true(self):
        self.assertTrue(True)

    def test_add_response(self):
        # Create AddResponse class instance
        test_model = AddResponse(member={"laudantium": 6})
        self.assertEqual(test_model.member, {"laudantium": 6})


if __name__ == "__main__":
    unittest.main()

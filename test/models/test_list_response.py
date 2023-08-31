import unittest
from src.dopplersdk.models.ListResponse import ListResponse


class TestListResponseModel(unittest.TestCase):
    def test_true(self):
        self.assertTrue(True)

    def test_list_response(self):
        # Create ListResponse class instance
        test_model = ListResponse(groups=["a", "asperiores"])
        self.assertEqual(test_model.groups, ["a", "asperiores"])


if __name__ == "__main__":
    unittest.main()

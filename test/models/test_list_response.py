import unittest
from src.dopplersdk.models.ListResponse import ListResponse


class TestListResponseModel(unittest.TestCase):
    def test_true(self):
        self.assertTrue(True)

    def test_list_response(self):
        # Create ListResponse class instance
        test_model = ListResponse(page=4, projects=["inventore", "officia"])
        self.assertEqual(test_model.page, 4)
        self.assertEqual(test_model.projects, ["inventore", "officia"])


if __name__ == "__main__":
    unittest.main()

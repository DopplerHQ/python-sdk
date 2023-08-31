import unittest
from src.dopplersdk.models.RenameResponse import RenameResponse


class TestRenameResponseModel(unittest.TestCase):
    def test_true(self):
        self.assertTrue(True)

    def test_rename_response(self):
        # Create RenameResponse class instance
        test_model = RenameResponse(environment={"asperiores": 9})
        self.assertEqual(test_model.environment, {"asperiores": 9})


if __name__ == "__main__":
    unittest.main()

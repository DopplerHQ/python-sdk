import unittest
from src.dopplersdk.models.WorkplaceUpdateResponse import WorkplaceUpdateResponse


class TestWorkplaceUpdateResponseModel(unittest.TestCase):
    def test_true(self):
        self.assertTrue(True)

    def test_workplace_update_response(self):
        # Create WorkplaceUpdateResponse class instance
        test_model = WorkplaceUpdateResponse(workplace={"delectus": 5})
        self.assertEqual(test_model.workplace, {"delectus": 5})


if __name__ == "__main__":
    unittest.main()

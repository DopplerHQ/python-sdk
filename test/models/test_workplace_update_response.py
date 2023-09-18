import unittest
from src.dopplersdk.models.WorkplaceUpdateResponse import WorkplaceUpdateResponse


class TestWorkplaceUpdateResponseModel(unittest.TestCase):
    def test_true(self):
        self.assertTrue(True)

    def test_workplace_update_response(self):
        # Create WorkplaceUpdateResponse class instance
        test_model = WorkplaceUpdateResponse(workplace={"ipsa": 5})
        self.assertEqual(test_model.workplace, {"ipsa": 5})


if __name__ == "__main__":
    unittest.main()

import unittest
from src.dopplersdk.models.WorkplaceGetResponse import WorkplaceGetResponse


class TestWorkplaceGetResponseModel(unittest.TestCase):
    def test_true(self):
        self.assertTrue(True)

    def test_workplace_get_response(self):
        # Create WorkplaceGetResponse class instance
        test_model = WorkplaceGetResponse(workplace={"animi": 2})
        self.assertEqual(test_model.workplace, {"animi": 2})


if __name__ == "__main__":
    unittest.main()

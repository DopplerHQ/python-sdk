import unittest
from src.dopplersdk.models.SyncsGetResponse import SyncsGetResponse


class TestSyncsGetResponseModel(unittest.TestCase):
    def test_true(self):
        self.assertTrue(True)

    def test_syncs_get_response(self):
        # Create SyncsGetResponse class instance
        test_model = SyncsGetResponse(sync={"quam": 2})
        self.assertEqual(test_model.sync, {"quam": 2})


if __name__ == "__main__":
    unittest.main()

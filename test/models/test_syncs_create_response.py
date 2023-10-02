import unittest
from src.dopplersdk.models.SyncsCreateResponse import SyncsCreateResponse


class TestSyncsCreateResponseModel(unittest.TestCase):
    def test_true(self):
        self.assertTrue(True)

    def test_syncs_create_response(self):
        # Create SyncsCreateResponse class instance
        test_model = SyncsCreateResponse(sync={"quas": 3})
        self.assertEqual(test_model.sync, {"quas": 3})


if __name__ == "__main__":
    unittest.main()

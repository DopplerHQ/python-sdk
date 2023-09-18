import unittest
from src.dopplersdk.models.SyncsCreateResponse import SyncsCreateResponse


class TestSyncsCreateResponseModel(unittest.TestCase):
    def test_true(self):
        self.assertTrue(True)

    def test_syncs_create_response(self):
        # Create SyncsCreateResponse class instance
        test_model = SyncsCreateResponse(sync={"recusandae": 8})
        self.assertEqual(test_model.sync, {"recusandae": 8})


if __name__ == "__main__":
    unittest.main()

import unittest
from src.dopplersdk.models.SyncsCreateRequest import SyncsCreateRequest


class TestSyncsCreateRequestModel(unittest.TestCase):
    def test_true(self):
        self.assertTrue(True)

    def test_syncs_create_request(self):
        # Create SyncsCreateRequest class instance
        test_model = SyncsCreateRequest(
            data={"provident": 9}, integration="dignissimos", import_option="none"
        )
        self.assertEqual(test_model.data, {"provident": 9})
        self.assertEqual(test_model.integration, "dignissimos")
        self.assertEqual(test_model.import_option, "none")

    def test_syncs_create_request_required_fields_missing(self):
        # Assert SyncsCreateRequest class generation fails without required fields
        with self.assertRaises(TypeError):
            test_model = SyncsCreateRequest()


if __name__ == "__main__":
    unittest.main()

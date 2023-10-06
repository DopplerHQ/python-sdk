import unittest
from src.dopplersdk.models.UpdateRequest import UpdateRequest


class TestUpdateRequestModel(unittest.TestCase):
    def test_true(self):
        self.assertTrue(True)

    def test_update_request(self):
        # Create UpdateRequest class instance
        test_model = UpdateRequest(
            secrets={"ipsam": 3}, config="deleniti", project="placeat"
        )
        self.assertEqual(test_model.secrets, {"ipsam": 3})
        self.assertEqual(test_model.config, "deleniti")
        self.assertEqual(test_model.project, "placeat")

    def test_update_request_required_fields_missing(self):
        # Assert UpdateRequest class generation fails without required fields
        with self.assertRaises(TypeError):
            test_model = UpdateRequest()


if __name__ == "__main__":
    unittest.main()

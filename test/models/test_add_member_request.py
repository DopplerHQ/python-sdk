import unittest
from src.dopplersdk.models.AddMemberRequest import AddMemberRequest


class TestAddMemberRequestModel(unittest.TestCase):
    def test_true(self):
        self.assertTrue(True)

    def test_add_member_request(self):
        # Create AddMemberRequest class instance
        test_model = AddMemberRequest(type_="workplace_user", slug="blanditiis")
        self.assertEqual(test_model.type_, "workplace_user")
        self.assertEqual(test_model.slug, "blanditiis")

    def test_add_member_request_required_fields_missing(self):
        # Assert AddMemberRequest class generation fails without required fields
        with self.assertRaises(TypeError):
            test_model = AddMemberRequest()


if __name__ == "__main__":
    unittest.main()

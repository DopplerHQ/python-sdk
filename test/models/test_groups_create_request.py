import unittest
from src.dopplersdk.models.GroupsCreateRequest import GroupsCreateRequest


class TestGroupsCreateRequestModel(unittest.TestCase):
    def test_true(self):
        self.assertTrue(True)

    def test_groups_create_request(self):
        # Create GroupsCreateRequest class instance
        test_model = GroupsCreateRequest(
            name="placeat", default_project_role="consequuntur"
        )
        self.assertEqual(test_model.name, "placeat")
        self.assertEqual(test_model.default_project_role, "consequuntur")

    def test_groups_create_request_required_fields_missing(self):
        # Assert GroupsCreateRequest class generation fails without required fields
        with self.assertRaises(TypeError):
            test_model = GroupsCreateRequest()


if __name__ == "__main__":
    unittest.main()

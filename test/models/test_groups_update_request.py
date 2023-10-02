import unittest
from src.dopplersdk.models.GroupsUpdateRequest import GroupsUpdateRequest


class TestGroupsUpdateRequestModel(unittest.TestCase):
    def test_true(self):
        self.assertTrue(True)

    def test_groups_update_request(self):
        # Create GroupsUpdateRequest class instance
        test_model = GroupsUpdateRequest(name="laborum", default_project_role="soluta")
        self.assertEqual(test_model.name, "laborum")
        self.assertEqual(test_model.default_project_role, "soluta")


if __name__ == "__main__":
    unittest.main()

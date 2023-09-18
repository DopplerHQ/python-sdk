import unittest
from src.dopplersdk.models.GroupsUpdateResponse import GroupsUpdateResponse


class TestGroupsUpdateResponseModel(unittest.TestCase):
    def test_true(self):
        self.assertTrue(True)

    def test_groups_update_response(self):
        # Create GroupsUpdateResponse class instance
        test_model = GroupsUpdateResponse(group={"suscipit": 8})
        self.assertEqual(test_model.group, {"suscipit": 8})


if __name__ == "__main__":
    unittest.main()

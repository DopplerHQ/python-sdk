import unittest
from src.dopplersdk.models.GroupsListResponse import GroupsListResponse


class TestGroupsListResponseModel(unittest.TestCase):
    def test_true(self):
        self.assertTrue(True)

    def test_groups_list_response(self):
        # Create GroupsListResponse class instance
        test_model = GroupsListResponse(groups=["voluptate", "nulla"])
        self.assertEqual(test_model.groups, ["voluptate", "nulla"])


if __name__ == "__main__":
    unittest.main()

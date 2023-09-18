import unittest
from src.dopplersdk.models.GroupsGetResponse import GroupsGetResponse


class TestGroupsGetResponseModel(unittest.TestCase):
    def test_true(self):
        self.assertTrue(True)

    def test_groups_get_response(self):
        # Create GroupsGetResponse class instance
        test_model = GroupsGetResponse(group={"perferendis": 7})
        self.assertEqual(test_model.group, {"perferendis": 7})


if __name__ == "__main__":
    unittest.main()

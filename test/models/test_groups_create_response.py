import unittest
from src.dopplersdk.models.GroupsCreateResponse import GroupsCreateResponse


class TestGroupsCreateResponseModel(unittest.TestCase):
    def test_true(self):
        self.assertTrue(True)

    def test_groups_create_response(self):
        # Create GroupsCreateResponse class instance
        test_model = GroupsCreateResponse(group={"dolores": 9})
        self.assertEqual(test_model.group, {"dolores": 9})


if __name__ == "__main__":
    unittest.main()

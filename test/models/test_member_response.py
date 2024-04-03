import unittest
from src.dopplersdk.models.MemberResponse import MemberResponse


class TestMemberResponseModel(unittest.TestCase):
    def test_true(self):
        self.assertTrue(True)

    def test_member_response(self):
        # Create MemberResponse class instance
        test_model = MemberResponse(group={"ad": 9})
        self.assertEqual(test_model.group, {"ad": 9})


if __name__ == "__main__":
    unittest.main()

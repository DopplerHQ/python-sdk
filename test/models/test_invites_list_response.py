import unittest
from src.dopplersdk.models.InvitesListResponse import InvitesListResponse


class TestInvitesListResponseModel(unittest.TestCase):
    def test_true(self):
        self.assertTrue(True)

    def test_invites_list_response(self):
        # Create InvitesListResponse class instance
        test_model = InvitesListResponse(invites=["deleniti", "maiores"])
        self.assertEqual(test_model.invites, ["deleniti", "maiores"])


if __name__ == "__main__":
    unittest.main()

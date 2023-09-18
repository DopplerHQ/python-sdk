import unittest
from src.dopplersdk.models.InvitesListResponse import InvitesListResponse


class TestInvitesListResponseModel(unittest.TestCase):
    def test_true(self):
        self.assertTrue(True)

    def test_invites_list_response(self):
        # Create InvitesListResponse class instance
        test_model = InvitesListResponse(invites=["quo", "doloremque"])
        self.assertEqual(test_model.invites, ["quo", "doloremque"])


if __name__ == "__main__":
    unittest.main()

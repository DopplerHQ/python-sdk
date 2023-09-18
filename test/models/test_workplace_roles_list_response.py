import unittest
from src.dopplersdk.models.WorkplaceRolesListResponse import WorkplaceRolesListResponse


class TestWorkplaceRolesListResponseModel(unittest.TestCase):
    def test_true(self):
        self.assertTrue(True)

    def test_workplace_roles_list_response(self):
        # Create WorkplaceRolesListResponse class instance
        test_model = WorkplaceRolesListResponse(roles=["fugiat", "laborum"])
        self.assertEqual(test_model.roles, ["fugiat", "laborum"])


if __name__ == "__main__":
    unittest.main()

import unittest
from src.dopplersdk.models.WorkplaceRolesGetResponse import WorkplaceRolesGetResponse


class TestWorkplaceRolesGetResponseModel(unittest.TestCase):
    def test_true(self):
        self.assertTrue(True)

    def test_workplace_roles_get_response(self):
        # Create WorkplaceRolesGetResponse class instance
        test_model = WorkplaceRolesGetResponse(role={"modi": 8})
        self.assertEqual(test_model.role, {"modi": 8})


if __name__ == "__main__":
    unittest.main()

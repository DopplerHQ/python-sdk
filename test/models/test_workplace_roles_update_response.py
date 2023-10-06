import unittest
from src.dopplersdk.models.WorkplaceRolesUpdateResponse import (
    WorkplaceRolesUpdateResponse,
)


class TestWorkplaceRolesUpdateResponseModel(unittest.TestCase):
    def test_true(self):
        self.assertTrue(True)

    def test_workplace_roles_update_response(self):
        # Create WorkplaceRolesUpdateResponse class instance
        test_model = WorkplaceRolesUpdateResponse(role={"eum": 4})
        self.assertEqual(test_model.role, {"eum": 4})


if __name__ == "__main__":
    unittest.main()

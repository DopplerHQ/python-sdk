import unittest
from src.dopplersdk.models.WorkplaceRolesUpdateResponse import (
    WorkplaceRolesUpdateResponse,
)


class TestWorkplaceRolesUpdateResponseModel(unittest.TestCase):
    def test_true(self):
        self.assertTrue(True)

    def test_workplace_roles_update_response(self):
        # Create WorkplaceRolesUpdateResponse class instance
        test_model = WorkplaceRolesUpdateResponse(role={"non": 1})
        self.assertEqual(test_model.role, {"non": 1})


if __name__ == "__main__":
    unittest.main()

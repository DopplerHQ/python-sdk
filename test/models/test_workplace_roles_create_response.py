import unittest
from src.dopplersdk.models.WorkplaceRolesCreateResponse import (
    WorkplaceRolesCreateResponse,
)


class TestWorkplaceRolesCreateResponseModel(unittest.TestCase):
    def test_true(self):
        self.assertTrue(True)

    def test_workplace_roles_create_response(self):
        # Create WorkplaceRolesCreateResponse class instance
        test_model = WorkplaceRolesCreateResponse(role={"neque": 3})
        self.assertEqual(test_model.role, {"neque": 3})


if __name__ == "__main__":
    unittest.main()

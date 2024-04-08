import unittest
from src.dopplersdk.models.WorkplaceRolesUpdateRequest import (
    WorkplaceRolesUpdateRequest,
)


class TestWorkplaceRolesUpdateRequestModel(unittest.TestCase):
    def test_true(self):
        self.assertTrue(True)

    def test_workplace_roles_update_request(self):
        # Create WorkplaceRolesUpdateRequest class instance
        test_model = WorkplaceRolesUpdateRequest(
            name="inventore", permissions=["qui", "iusto"]
        )
        self.assertEqual(test_model.name, "inventore")
        self.assertEqual(test_model.permissions, ["qui", "iusto"])


if __name__ == "__main__":
    unittest.main()

import unittest
from src.dopplersdk.models.WorkplaceRolesCreateRequest import (
    WorkplaceRolesCreateRequest,
)


class TestWorkplaceRolesCreateRequestModel(unittest.TestCase):
    def test_true(self):
        self.assertTrue(True)

    def test_workplace_roles_create_request(self):
        # Create WorkplaceRolesCreateRequest class instance
        test_model = WorkplaceRolesCreateRequest(
            permissions=["tempora", "saepe"], name="assumenda"
        )
        self.assertEqual(test_model.permissions, ["tempora", "saepe"])
        self.assertEqual(test_model.name, "assumenda")

    def test_workplace_roles_create_request_required_fields_missing(self):
        # Assert WorkplaceRolesCreateRequest class generation fails without required fields
        with self.assertRaises(TypeError):
            test_model = WorkplaceRolesCreateRequest()


if __name__ == "__main__":
    unittest.main()

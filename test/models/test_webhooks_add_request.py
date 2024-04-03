import unittest
from src.dopplersdk.models.WebhooksAddRequest import WebhooksAddRequest


class TestWebhooksAddRequestModel(unittest.TestCase):
    def test_true(self):
        self.assertTrue(True)

    def test_webhooks_add_request(self):
        # Create WebhooksAddRequest class instance
        test_model = WebhooksAddRequest(
            url="voluptatibus",
            secret="voluptate",
            authentication={"dolores": 5},
            payload="ea",
            enableConfigs=["atque", "accusamus"],
        )
        self.assertEqual(test_model.url, "voluptatibus")
        self.assertEqual(test_model.secret, "voluptate")
        self.assertEqual(test_model.authentication, {"dolores": 5})
        self.assertEqual(test_model.payload, "ea")
        self.assertEqual(test_model.enableConfigs, ["atque", "accusamus"])

    def test_webhooks_add_request_required_fields_missing(self):
        # Assert WebhooksAddRequest class generation fails without required fields
        with self.assertRaises(TypeError):
            test_model = WebhooksAddRequest()


if __name__ == "__main__":
    unittest.main()

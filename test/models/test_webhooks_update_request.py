import unittest
from src.dopplersdk.models.WebhooksUpdateRequest import WebhooksUpdateRequest


class TestWebhooksUpdateRequestModel(unittest.TestCase):
    def test_true(self):
        self.assertTrue(True)

    def test_webhooks_update_request(self):
        # Create WebhooksUpdateRequest class instance
        test_model = WebhooksUpdateRequest(
            url="debitis",
            secret="culpa",
            authentication={"animi": 5},
            payload="porro",
            enableConfigs=["neque", "similique"],
            disableConfigs=["ducimus", "pariatur"],
        )
        self.assertEqual(test_model.url, "debitis")
        self.assertEqual(test_model.secret, "culpa")
        self.assertEqual(test_model.authentication, {"animi": 5})
        self.assertEqual(test_model.payload, "porro")
        self.assertEqual(test_model.enableConfigs, ["neque", "similique"])
        self.assertEqual(test_model.disableConfigs, ["ducimus", "pariatur"])


if __name__ == "__main__":
    unittest.main()

import unittest
from src.dopplersdk.models.CreateResponse import CreateResponse


class TestCreateResponseModel(unittest.TestCase):
    def test_true(self):
        self.assertTrue(True)

    def test_create_response(self):
        # Create CreateResponse class instance
        test_model = CreateResponse(project={"dolore": 7})
        self.assertEqual(test_model.project, {"dolore": 7})


if __name__ == "__main__":
    unittest.main()

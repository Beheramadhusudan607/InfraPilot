import unittest
from app.app import app


class InfraPilotTests(unittest.TestCase):

    def setUp(self):
        self.client = app.test_client()

    def test_home_endpoint(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
        data = response.get_json()
        self.assertEqual(data["project"], "InfraPilot")
        self.assertEqual(data["status"], "running")

    def test_health_endpoint(self):
        response = self.client.get("/health")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_json()["status"], "healthy")


if __name__ == "__main__":
    unittest.main()

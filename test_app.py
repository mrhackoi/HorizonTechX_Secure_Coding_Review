
import os
import tempfile
import unittest

import app as demo


class SecureCodingTests(unittest.TestCase):
    def setUp(self):
        self.temp_dir = tempfile.TemporaryDirectory()
        demo.DB_PATH = os.path.join(self.temp_dir.name, "test.db")
        demo.app.config["TESTING"] = True
        demo.init_db()
        self.client = demo.app.test_client()

    def tearDown(self):
        self.temp_dir.cleanup()

    def test_health(self):
        response = self.client.get("/health")
        self.assertEqual(response.status_code, 200)

    def test_search_valid_query(self):
        response = self.client.get("/search?q=mouse")
        self.assertEqual(response.status_code, 200)
        self.assertIn("Mouse", response.get_data(as_text=True))

    def test_empty_search_rejected(self):
        response = self.client.get("/search?q=")
        self.assertEqual(response.status_code, 400)

    def test_long_search_rejected(self):
        response = self.client.get("/search?q=" + "a" * 101)
        self.assertEqual(response.status_code, 400)

    def test_registration_and_login(self):
        response = self.client.post("/register", json={
            "username": "testuser",
            "password": "DemoPass!2026Secure"
        })
        self.assertEqual(response.status_code, 201)

        response = self.client.post("/login", json={
            "username": "testuser",
            "password": "DemoPass!2026Secure"
        })
        self.assertEqual(response.status_code, 200)

    def test_wrong_password_rejected(self):
        self.client.post("/register", json={
            "username": "testuser",
            "password": "DemoPass!2026Secure"
        })
        response = self.client.post("/login", json={
            "username": "testuser",
            "password": "WrongPassword!123"
        })
        self.assertEqual(response.status_code, 401)


if __name__ == "__main__":
    unittest.main(verbosity=2)

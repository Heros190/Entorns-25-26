import unittest
from src.app import app
from src.dao.user_dao import UserDao

class AuthTestCase(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True
        self.user_dao = UserDao()

    def test_login_success(self):
        response = self.app.post('/login', json={
            'username': 'prova@gmail.com',
            'password': '12345'
        })
        self.assertEqual(response.status_code, 200)
        self.assertIn('coderesponse', response.get_json())
        self.assertEqual(response.get_json()['coderesponse'], '1')

    def test_login_failure(self):
        response = self.app.post('/login', json={
            'username': 'wronguser@gmail.com',
            'password': 'wrongpassword'
        })
        self.assertEqual(response.status_code, 400)
        self.assertIn('coderesponse', response.get_json())
        self.assertEqual(response.get_json()['coderesponse'], '0')

    def test_login_with_token_success(self):
        # Assuming a valid token is generated and stored
        token = 'token12345'
        response = self.app.post('/login', headers={'Authorization': token})
        self.assertEqual(response.status_code, 200)
        self.assertIn('coderesponse', response.get_json())
        self.assertEqual(response.get_json()['coderesponse'], '1')

    def test_login_with_token_failure(self):
        response = self.app.post('/login', headers={'Authorization': 'invalidtoken'})
        self.assertEqual(response.status_code, 400)
        self.assertIn('coderesponse', response.get_json())
        self.assertEqual(response.get_json()['coderesponse'], '0')

if __name__ == '__main__':
    unittest.main()
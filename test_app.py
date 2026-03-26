import unittest
from run import app
from app.extensions import db

class FlaskAppTests(unittest.TestCase):

    def setUp(self):
        app.config['TESTING'] = True
        app.config['WTF_CSRF_ENABLED'] = False
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
        self.client = app.test_client()
        
        with app.app_context():
            db.create_all()

    def tearDown(self):
        with app.app_context():
            db.session.remove()
            db.drop_all()

    def test_login_page(self):
        response = self.client.get('/login')
        self.assertEqual(response.status_code, 200)

    def test_register_page(self):
        response = self.client.get('/register') 
        self.assertEqual(response.status_code, 200)

    def test_api_students(self):
        response = self.client.get('/api/students')
        self.assertEqual(response.status_code, 200)

    def test_courses_page(self):
        response = self.client.get('/courses')
        self.assertEqual(response.status_code, 200)

    def test_add_course_page(self):
        response = self.client.get('/add_course')
        self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
    unittest.main()
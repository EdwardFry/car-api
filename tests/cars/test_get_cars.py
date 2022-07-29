from app import app
import unittest

class FlaskTestCase(unittest.TestCase):

    #  GET  /CARS
    def test_get_cars(self):
        tester = app.test_client(self)
        response = tester.get('/cars', follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertIsNotNone(response.json['data'])
        self.assertIsNotNone(response.json['status'])
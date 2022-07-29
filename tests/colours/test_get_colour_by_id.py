from app import app
import unittest

class FlaskTestCase(unittest.TestCase):
    
    # GET /COLOUR/<ID>
    def test_get_colour_by_id(self):
        tester = app.test_client(self)
        response = tester.get('/colour/0', follow_redirects=True)
        json = { 
                'status': 'ok',
                'data': 
                    {
                        'id': 0,
                        'name': 'red'
                    }
                }
        self.assertEqual(response.json, json)


    def test_get_car_by_incorrect_id(self):
        tester = app.test_client(self)
        response = tester.get('/colour/d', follow_redirects=True)
        self.assertEqual(response.status_code, 400)
    

    def test_get_car_no_id(self):
        tester = app.test_client(self)
        response = tester.get('/colour', follow_redirects=True)
        self.assertEqual(response.status_code, 404)
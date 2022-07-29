from app import app
import unittest

class FlaskTestCase(unittest.TestCase):
    
    #  GET  /CAR/<ID>
    def test_get_car_by_id(self):
        tester = app.test_client(self)
        response = tester.get('/car/1', follow_redirects=True)
        json = { 
                'status': 'ok',
                'data': 
                    {
                        'build_date': '25/09/2006', 
                        'colour_id': 1, 
                        'id': 1, 
                        'make': 'Ford', 
                        'model': 'GT'
                    }
                }
        self.assertEqual(response.json, json)


    def test_get_car_by_incorrect_id(self):
        tester = app.test_client(self)
        response = tester.get('/car/d', follow_redirects=True)
        self.assertEqual(response.status_code, 400)
    

    def test_get_car_no_id(self):
        tester = app.test_client(self)
        response = tester.get('/car', follow_redirects=True)
        self.assertEqual(response.status_code, 404)
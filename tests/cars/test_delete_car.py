from app import app
import unittest

class FlaskTestCase(unittest.TestCase):

    #  DELETE  /CAR/<ID>
    def test_delete(self):
        tester = app.test_client(self)
        response = tester.delete('/car/0', follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        
        #checks if car with id 0 was deleted
        response = tester.get('/car/0', follow_redirects=True)
        self.assertEqual(response.status_code, 404)


    def test_delete_invalid_id(self):
        tester = app.test_client(self)
        response = tester.delete('/car/-1', follow_redirects=True)
        self.assertEqual(response.status_code, 400)
        
    
    def test_delete_invalid_id_string(self):
        tester = app.test_client(self)
        response = tester.delete('/car/s', follow_redirects=True)
        self.assertEqual(response.status_code, 400)

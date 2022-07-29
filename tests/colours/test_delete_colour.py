from app import app
import unittest

class FlaskTestCase(unittest.TestCase):

    # DELETE /COLOUR/<ID>
    def test_delete(self):
        tester = app.test_client(self)
        response = tester.delete('/colour/1', follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        
        #checks if colour with id 0 was deleted
        response = tester.get('/colour/1', follow_redirects=True)
        self.assertEqual(response.status_code, 404)


    def test_delete_invalid_id(self):
        tester = app.test_client(self)
        response = tester.delete('/colour/-1', follow_redirects=True)
        self.assertEqual(response.status_code, 400)
        
    
    def test_delete_invalid_id_string(self):
        tester = app.test_client(self)
        response = tester.delete('/colour/s', follow_redirects=True)
        self.assertEqual(response.status_code, 400)
from app import app
import unittest

class FlaskTestCase(unittest.TestCase):
    
    # POST /colours
    def test_post_no_data(self):
        tester = app.test_client(self)
        response = tester.post('/colours', follow_redirects=True)
        self.assertEqual(response.status_code, 400)
    
    
    def test_post_full_data(self):
        tester = app.test_client(self)
        response = tester.post(
            '/colours',
            json = { 'colours': 
                    [
                        {
                            'name': 'orange'
                        },
                        {
                            'name': 'yellow', 
                        }
                    ]
                }
            ,follow_redirects=True)
        self.assertEqual(response.status_code, 200)
    
        #check if cars have been added
        response = tester.get('/colour/4', follow_redirects=True)
        self.assertEqual(response.status_code, 200)

        response = tester.get('/colour/5', follow_redirects=True)
        self.assertEqual(response.status_code, 200)


    def test_post_incorrect_format(self):
        tester = app.test_client(self)
        response = tester.post(
            '/colours',
            json = { 'colours': 
                    [
                        {
                            'texttt': 'orange', 
                        }
                    ]
                    }
            ,follow_redirects=True)
        self.assertEqual(response.status_code, 400)
    
    
    def test_post_incorrect_format(self):
        tester = app.test_client(self)
        response = tester.post(
            '/colours',
            json = { 'colours': 
                        {
                            'texttt': 'orange', 
                        }
                    }
            ,follow_redirects=True)
        self.assertEqual(response.status_code, 400)

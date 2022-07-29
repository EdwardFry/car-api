from app import app
import unittest

class FlaskTestCase(unittest.TestCase):
    
    #  POST  /CARS
    def test_post_cars_no_data(self):
        tester = app.test_client(self)
        response = tester.post('/cars', follow_redirects=True)
        self.assertEqual(response.status_code, 400)
    
    
    def test_post_cars_full_data(self):
        tester = app.test_client(self)
        response = tester.post(
            '/cars',
            json = { 'cars': 
                    [
                        {
                            'make': 'Ford', 
                            'model': 'Fiesta', 
                            'build_date': '24/03/2018', 
                            'colour_id': 1
                        },
                        {
                            'make': 'Ford', 
                            'model': 'Fiesta', 
                            'build_date': '24/03/2018', 
                            'colour_id': 1
                        }
                    ]
                }
            ,follow_redirects=True)
        self.assertEqual(response.status_code, 200)
    
        #check if cars have been added
        response = tester.get('/car/4', follow_redirects=True)
        self.assertEqual(response.status_code, 200)

        response = tester.get('/car/5', follow_redirects=True)
        self.assertEqual(response.status_code, 200)


    def test_post_incorrect_format(self):
        tester = app.test_client(self)
        response = tester.post(
            '/cars',
            json = { 'cars': 
                    [
                        {
                            'makee': 'Ford', 
                            'model': 'Fiesta', 
                            'build_date': '24/03/2018', 
                            'colour_id': 1
                        },
                        {
                            'make': 'Ford', 
                            'model': 'Fiesta', 
                            'build_date': '24/03/2018', 
                            'colour_id': 1
                        }
                    ]
                    }
            ,follow_redirects=True)
        self.assertEqual(response.status_code, 400)
    

    def test_post_incorrect_colour_id_type(self):
        tester = app.test_client(self)
        response = tester.post(
            '/cars',
            json = { 'cars': 
                    [
                        {
                            'makee': 'Ford', 
                            'model': 'Fiesta', 
                            'build_date': '24/03/2018', 
                            'colour_id': '@'
                        },
                        {
                            'make': 'Ford', 
                            'model': 'Fiesta', 
                            'build_date': '24/03/2018', 
                            'colour_id': 1
                        }
                    ]
                    }
            ,follow_redirects=True)
        self.assertEqual(response.status_code, 400)
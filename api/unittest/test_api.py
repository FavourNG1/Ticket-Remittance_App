import unittest
from app import app, db

class APITestCase(unittest.TestCase):
    
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True
        # Other setup code (e.g., create tables)
    
    def tearDown(self):
        # Teardown code (e.g., drop tables)
        pass
    
    def test_get_tickets(self):
        response = self.app.get('/api/tickets')
        self.assertEqual(response.status_code, 200)
    
    def test_create_ticket(self):
        response = self.app.post('/api/tickets', json={
            'event_name': 'Concert',
            'purchaser_name': 'John Doe',
            'amount': 100.0
        })
        self.assertEqual(response.status_code, 201)

if __name__ == '__main__':
    unittest.main()

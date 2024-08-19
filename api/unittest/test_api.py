import unittest
from app import app, db, Ticket

class APITestCase(unittest.TestCase):
    
    def setUp(self):
        # Initialize a test client
        self.app = app.test_client()
        self.app.testing = True

        # Create the database and tables
        with app.app_context():
            db.create_all()

    def tearDown(self):
        # Drop all tables
        with app.app_context():
            db.session.remove()
            db.drop_all()

    def test_get_tickets(self):
        response = self.app.get('/api/tickets')
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.json, list)

    def test_create_ticket(self):
        response = self.app.post('/api/tickets', json={
            'event_name': 'Concert',
            'purchaser_name': 'John Doe',
            'amount': 100.0
        })
        self.assertEqual(response.status_code, 201)
        self.assertIn('event_name', response.json)

if __name__ == '__main__':
    unittest.main()

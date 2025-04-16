import unittest
from app import create_app

class CalculatorTestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.app = create_app()
        cls.client = cls.app.test_client()

    def test_addition(self):
        response = self.client.post('/calculate', data={'a': 5, 'b': 3, 'operation': '+'})
        self.assertIn('8.0', response.data.decode('utf-8'))

    def test_subtraction(self):
        response = self.client.post('/calculate', data={'a': 5, 'b': 3, 'operation': '-'})
        self.assertIn('2.0', response.data.decode('utf-8'))

    def test_multiplication(self):
        response = self.client.post('/calculate', data={'a': 5, 'b': 3, 'operation': '*'})
        self.assertIn('15.0', response.data.decode('utf-8'))

    def test_division(self):
        response = self.client.post('/calculate', data={'a': 6, 'b': 3, 'operation': '/'})
        self.assertIn('2.0', response.data.decode('utf-8'))

    def test_division_by_zero(self):
        response = self.client.post('/calculate', data={'a': 5, 'b': 0, 'operation': '/'})
        self.assertIn('Ошибка: деление на ноль', response.data.decode('utf-8'))

    def test_invalid_operation(self):
        response = self.client.post('/calculate', data={'a': 5, 'b': 3, 'operation': '^'})
        self.assertIn('Недопустимая операция', response.data.decode('utf-8'))

    def setUp(self):
        self.app = create_app().test_client()
        self.app.testing = True

    def test_power_calculation(self):
        response = self.app.post('/power', data=dict(base=2, exponent=3))
        self.assertEqual(response.status_code, 200)
        self.assertIn('Результат: 8.0', response.data)
    
if __name__ == "__main__":
    unittest.main()

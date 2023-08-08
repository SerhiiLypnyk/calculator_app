from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APITestCase, APIClient
from rest_framework.views import status
from .models import calculate, OPERATIONS


class CalculatorModelTest(TestCase):
    def test_calculate_addition(self):
        self.assertEqual(calculate("+", 1, 2), 3)

    def test_calculate_subtraction(self):
        self.assertEqual(calculate("-", 5, 2), 3)

    def test_calculate_multiplication(self):
        self.assertEqual(calculate("*", 3, 3), 9)

    def test_calculate_division(self):
        self.assertEqual(calculate("/", 10, 2), 5)

    def test_calculate_division_by_zero(self):
        self.assertEqual(calculate("/", 10, 0), "Division by zero")


class CalculatorViewSetTest(APITestCase):
    def setUp(self):
        self.client = APIClient()

    def test_calculate_endpoint(self):
        # Test addition
        response = self.client.post(reverse('calculator-calculate'), {
            'operation': '+',
            'operand1': 5,
            'operand2': 3,
        })
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, {'result': '8.0', 'result_type': 'float'})

        # Test subtraction
        response = self.client.post(reverse('calculator-calculate'), {
            'operation': '-',
            'operand1': 7,
            'operand2': 2,
        })
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, {'result': '5.0', 'result_type': 'float'})

        # Test multiplication
        response = self.client.post(reverse('calculator-calculate'), {
            'operation': '*',
            'operand1': 4,
            'operand2': 6,
        })
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, {'result': '24.0', 'result_type': 'float'})

        # Test division
        response = self.client.post(reverse('calculator-calculate'), {
            'operation': '/',
            'operand1': 10,
            'operand2': 2,
        })
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, {'result': '5.0', 'result_type': 'float'})

        # Test division by zero
        response = self.client.post(reverse('calculator-calculate'), {
            'operation': '/',
            'operand1': 10,
            'operand2': 0,
        })
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, {'result': "Division by zero", 'result_type': 'str'})

        # Test invalid operation
        response = self.client.post(reverse('calculator-calculate'), {
            'operation': '%',  # Assuming modulus operation isn't supported
            'operand1': 10,
            'operand2': 3,
        })
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('operation', response.data)

        # Test without providing operand1
        response = self.client.post(reverse('calculator-calculate'), {
            'operation': '+',
            'operand2': 3,
        })
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('operand1', response.data)

        # Test without providing operand2
        response = self.client.post(reverse('calculator-calculate'), {
            'operation': '+',
            'operand1': 5,
        })
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('operand2', response.data)

        # Test without providing operation
        response = self.client.post(reverse('calculator-calculate'), {
            'operand1': 5,
            'operand2': 3,
        })
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('operation', response.data)

    def test_operations_endpoint(self):
        response = self.client.get(reverse('calculator-operations'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(set(response.data), set(OPERATIONS.keys()))

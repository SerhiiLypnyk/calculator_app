from django.urls import reverse
from rest_framework.test import APITestCase, APIClient
from rest_framework import status

from app.models import Calculator


class CalculatorViewSetTests(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.calculator_instance = Calculator()

    def test_addition(self):
        response = self.client.post(reverse('calculator-calculate'), {'expression': '3+2'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['result'], 5.0)

    def test_subtraction(self):
        response = self.client.post(reverse('calculator-calculate'), {'expression': '5-3'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['result'], 2.0)

    def test_multiplication(self):
        response = self.client.post(reverse('calculator-calculate'), {'expression': '2*4'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['result'], 8.0)

    def test_division(self):
        response = self.client.post(reverse('calculator-calculate'), {'expression': '8/2'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['result'], 4.0)

    def test_division_by_zero(self):
        response = self.client.post(reverse('calculator-calculate'), {'expression': '5/0'})
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data['error'], 'Division by zero')

    def test_mismatched_parentheses(self):
        response = self.client.post(reverse('calculator-calculate'), {'expression': '5+(3*2'})
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data['error'], 'Mismatched parentheses')

    def test_complex_expression(self):
        response = self.client.post(reverse('calculator-calculate'), {'expression': '0-(100/2+92*0.5)'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['result'], -96.0)

    def test_available_operations(self):
        response = self.client.get(reverse('calculator-operations'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        expected_operations = self.calculator_instance.operations
        self.assertListEqual(response.data['available_operations'], list(expected_operations))

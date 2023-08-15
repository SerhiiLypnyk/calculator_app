from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

from .models import Calculator


class CalculatorViewSet(viewsets.ViewSet):
    calculator_instance = Calculator()

    @swagger_auto_schema(
        operation_description="Performs a calculation based on the given expression",
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            required=['expression'],
            properties={
                'expression': openapi.Schema(type=openapi.TYPE_STRING, description='Expression to evaluate'),
            },
        ),
        responses={
            200: openapi.Schema(
                type=openapi.TYPE_OBJECT,
                properties={
                    'result': openapi.Schema(type=openapi.TYPE_NUMBER, description='Result of the calculation'),
                    'result_type': openapi.Schema(type=openapi.TYPE_STRING, description='Type of the result'),
                }
            ),
            400: "Error: Bad request"
        }
    )
    @action(detail=False, methods=['post'])
    def calculate(self, request):
        expression = str(request.data.get('expression'))
        if not expression:
            return Response({"error": "Expression is required."}, status=400)
        try:
            postfix_expression = self.calculator_instance.infix_to_postfix(expression)
            result = self.calculator_instance.calculate(postfix_expression)
            result_type = type(result).__name__
            return Response({"result": result, "result_type": result_type})
        except Exception as e:
            return Response({"error": str(e)}, status=400)

    @action(detail=False, methods=['get'])
    def operations(self, request):
        operations = list(self.calculator_instance.operations.keys())
        return Response({"available_operations": operations})

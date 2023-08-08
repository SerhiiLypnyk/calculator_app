from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

from .models import OPERATIONS, calculate
from .serializers import CalculatorInput, CalculatorOutput


class CalculatorViewSet(viewsets.ViewSet):
    """
    A simple ViewSet for performing calculator operations.
    """

    @swagger_auto_schema(
        operation_description="Performs a calculation based on the given operation and operands.",
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            required=['operand1', 'operand2', 'operation'],
            properties={
                'operand1': openapi.Schema(type=openapi.TYPE_NUMBER, description='First operand'),
                'operand2': openapi.Schema(type=openapi.TYPE_NUMBER, description='Second operand'),
                'operation': openapi.Schema(
                    type=openapi.TYPE_STRING, description=f'Operation to perform: {list(OPERATIONS.keys())}'
                ),
            },
        ),
        responses={200: CalculatorOutput()},
    )
    @action(detail=False, methods=['post'])
    def calculate(self, request):
        serializer = CalculatorInput(data=request.data)
        if serializer.is_valid():
            operation = serializer.validated_data['operation']
            operand1 = serializer.validated_data['operand1']
            operand2 = serializer.validated_data['operand2']
            result = calculate(operation, operand1, operand2)
            result_type = type(result).__name__
            output_serializer = CalculatorOutput({
                'result': result,
                'result_type': result_type
            })
            return Response(output_serializer.data)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=False, methods=['get'])
    def operations(self, request):
        """
        Returns a list of all available operations.
        """
        return Response(list(OPERATIONS.keys()))

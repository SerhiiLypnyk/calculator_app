from rest_framework import serializers

from .models import OPERATIONS


class CalculatorInput(serializers.Serializer):
    operation = serializers.ChoiceField(choices=[(op, op) for op in OPERATIONS.keys()])
    operand1 = serializers.FloatField()
    operand2 = serializers.FloatField()


class CalculatorOutput(serializers.Serializer):
    result = serializers.CharField()
    result_type = serializers.CharField()

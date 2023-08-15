import re
from collections import deque


class Operator:
    precedence = 0

    def evaluate(self, a, b):
        raise NotImplementedError

    @classmethod
    def get_precedence(cls):
        return cls.precedence


class Add(Operator):
    precedence = 1

    def evaluate(self, a, b):
        return a + b


class Subtract(Operator):
    precedence = 1

    def evaluate(self, a, b):
        return a - b


class Multiply(Operator):
    precedence = 2

    def evaluate(self, a, b):
        return a * b


class Divide(Operator):
    precedence = 2

    def evaluate(self, a, b):
        if b == 0:
            raise ValueError("Division by zero")
        return a / b


class Calculator:
    def __init__(self):
        self.operations = {
            '+': Add(),
            '-': Subtract(),
            '*': Multiply(),
            '/': Divide(),
        }

    @staticmethod
    def tokenize(expression):
        tokens = re.findall(r"(\d+\.\d+|\d+|[+\-*/()])", expression)
        for token in tokens:
            yield token

    def infix_to_postfix(self, expression):
        def is_operator(token):
            return token in self.operations

        output = []
        operators = deque()

        for token in self.tokenize(expression):
            if token.isdigit() or '.' in token:
                output.append(token)
            elif is_operator(token):
                while (operators
                       and is_operator(operators[-1])
                       and self.operations[operators[-1]].get_precedence() >= self.operations[token].get_precedence()):
                    output.append(operators.pop())
                operators.append(token)
            elif token == '(':
                operators.append(token)
            elif token == ')':
                while operators and operators[-1] != '(':
                    output.append(operators.pop())
                if not operators:
                    raise ValueError("Mismatched parentheses")
                operators.pop()

        while operators:
            if operators[-1] in ['(', ')']:
                raise ValueError("Mismatched parentheses")
            output.append(operators.pop())

        return output

    def calculate(self, postfix):
        stack = []

        for token in postfix:
            if token in self.operations:
                b = stack.pop()
                a = stack.pop()
                result = self.operations[token].evaluate(a, b)
                stack.append(result)
            else:
                stack.append(float(token))

        return stack[0]

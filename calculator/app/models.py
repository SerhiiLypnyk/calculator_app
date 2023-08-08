class Operation:
    def execute(self, a, b):
        raise NotImplementedError


class Add(Operation):
    def execute(self, a, b):
        return a + b


class Subtract(Operation):
    def execute(self, a, b):
        return a - b


class Multiply(Operation):
    def execute(self, a, b):
        return a * b


class Divide(Operation):
    def execute(self, a, b):
        return a / b if b != 0 else "Division by zero"


OPERATIONS = {
    '+': Add(),
    '-': Subtract(),
    '*': Multiply(),
    '/': Divide(),
}


def calculate(operation, a, b):
    return OPERATIONS[operation].execute(a, b)

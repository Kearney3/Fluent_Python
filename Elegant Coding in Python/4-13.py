"""使用__call__改变类的行为"""


class Calculation:
    def __init__(self, operation):
        self.operation = operation

    def __call__(self, first_number, second_number):
        if isinstance(first_number, int) and isinstance(second_number, int):
            return self.operation()
        raise ValueError("Only integers are allowed")

    def add(self, first_number, second_number):
        return first_number + second_number

    def mutiply(self, first_number, second_number):
        return first_number * second_number

add = Calculation.add()
print(add(4,5))
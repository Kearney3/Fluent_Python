"""迭代器类"""

class Mutiply:
    def __init__(self, number):
        self.number = number
        self.count = 0

    def __next__(self):
        self.count += 1
        return self.number * self.count

mul = Mutiply(5)
print(next(mul))
print(next(mul))
print(next(mul))